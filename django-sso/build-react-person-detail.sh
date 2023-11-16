reactProjectName="react-person-detail";
reactOut="$reactProjectName/dist";
reactOutAssets="$reactProjectName/dist/assets";
djangoRootName="springmicro_crm";
djangoProjectName="springmicro_crm";
djangoProjectDir="$djangoRootName/$djangoProjectName";
djangoTemplatesDir="$djangoProjectDir/templates";
djangoStaticDir="$djangoProjectDir/static";
djangoStaticReactDir="$djangoStaticDir/$reactProjectName"
outHtmlFile="$reactProjectName.html"

# REACT
cd $reactProjectName;
# outputs to $reactOut
# index.html, assets/index-hash.css, assets/index-hash.js
pnpm run build;
input_file="dist/index.html"

# rename assets dir to reactProjectName
# mv "dist/assets" "dist/$reactProjectName"
sed -i "s/\/assets/$reactProjectName/g" "$input_file"

# Extract values from Format 1
javascript=$(grep -oP '<script type="module" crossorigin src="[^"]+' "$input_file" | sed 's/<script type="module" crossorigin src="//')
css=$(grep -oP '<link rel="stylesheet" href="[^"]+' "$input_file" | sed 's/<link rel="stylesheet" href="//')

# Create Format 2 content
meta="{% extends \"base.html\" %}\n{% load static %}\n"
javascript_block="{% block javascript %}<script type=\"module\" crossorigin src=\"{% static '$javascript' %}\"></script>{% endblock %}"
css_block="{% block css %}<link rel=\"stylesheet\" href=\"{% static '$css' %}\">{% endblock %}"
content_block="{% block content %}<div id=\"root\"></div>{% endblock %}"

# Write Format 2 content
echo -e "$meta\n$javascript_block\n$css_block\n$content_block" > $input_file;

# Finished
cd ..
pwd
##### END REACT

##### DJANGO

# template destination
mkdir -p $djangoTemplatesDir;
# copy files
# template
cp "$reactOut/index.html" "$djangoTemplatesDir/$outHtmlFile"
# assets
rm -rf $djangoStaticReactDir;
mv $reactOutAssets $djangoStaticReactDir;