import React from "react";
import { Input, Typography, Button } from "@material-tailwind/react";
import { FormikProps, useFormik } from "formik";

type InputEditProps = {
  type: string;
  name: string;
  labelText: string;
  editing: boolean;
  formik: FormikProps<any>;
  required?: boolean;
  inputProps?: any;
};

function ensureValidHref(href: string): string {
  // Regular expression for a simple URL pattern
  var urlPattern = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*\/?$/;

  // Check if the provided href matches the URL pattern
  if (!urlPattern.test(href)) {
    // If not, prepend "http://"
    href = "http://" + href;
  }

  return href;
}

function InputEdit(props: InputEditProps) {
  const { editing, type, name, labelText, formik, required, inputProps } =
    props;
  const id = `id_${name}`;
  const value = formik.values[name as keyof typeof formik] ?? "";
  if (editing) {
    return (
      <Input
        {...inputProps}
        id={id}
        label={labelText}
        name={name}
        labelProps={{ for: id }}
        value={value}
        type={type}
        required={required}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
    );
  } else {
    return (
      <div>
        <Typography variant="small" as="label" color="gray">
          {labelText}
        </Typography>
        {type === "url" ? (
          <a
            href={ensureValidHref(value)}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 dark:text-blue-500 hover:underline"
          >
            {value}
          </a>
        ) : (
          <Typography>{value}</Typography>
        )}
      </div>
    );
  }
}

export default function App() {
  const [editing, setEditing] = React.useState(false);
  const initialValues = {
    first_name: "Rob",
    last_name: "Dillman",
    business_name: "Magellan",
  };
  const formik = useFormik({
    initialValues,
    onSubmit: async (values, helpers) => {
      setEditing(false);
      console.log(values);
      console.log(helpers);
    },
  });

  const editButton = () => {
    if (editing) {
      // cancel
      formik.setValues(initialValues);
    }
    setEditing(!editing);
  };

  return (
    <>
      <form onSubmit={formik.handleSubmit}>
        <div className="mb-2 flex gap-2">
          <Button onClick={editButton}>{editing ? "Cancel" : "Edit"}</Button>
          {editing && <Button type="submit">Save</Button>}
        </div>
        <div className="flex flex-col gap-3">
          <InputEdit
            editing={editing}
            formik={formik}
            name="first_name"
            labelText="First Name"
            type="text"
            required
            inputProps={{
              maxlength: "50",
            }}
          />
          <InputEdit
            editing={editing}
            formik={formik}
            name="last_name"
            labelText="Last Name"
            type="text"
            required
            inputProps={{
              maxlength: "50",
            }}
          />
          <InputEdit
            editing={editing}
            formik={formik}
            name="business_name"
            labelText="Business Name"
            type="text"
            required
            inputProps={{
              maxlength: "75",
            }}
          />
          <InputEdit
            editing={editing}
            formik={formik}
            name="url"
            labelText="Website"
            type="url"
            required
            inputProps={{
              maxlength: "200",
            }}
          />
        </div>
      </form>
    </>
  );
}
