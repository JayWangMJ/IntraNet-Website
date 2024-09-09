---
# leave the title empty to use site title
title: 
date: 2022-10-24

type: landing

sections:
  - block: hero
    content:
      title: |
        About us
      align: center
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        Welcome to the **SMGE Research Lab**, where cutting-edge innovation meets real-world impact. At the crossroads of smart mobility, games, and economics, we are driving forward the future of technology and decision-making. Our interdisciplinary team of researchers and problem-solvers is dedicated to creating smarter, more connected systems that enrich lives and transform industries.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: event
    design:
      view: card
      columns: '1'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text: |
  #       {{% cta cta_link="../people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="../people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---