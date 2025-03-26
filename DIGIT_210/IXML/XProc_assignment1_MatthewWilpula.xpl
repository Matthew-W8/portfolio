<?xml version="1.0" encoding="UTF-8"?>
<p:declare-step xmlns:p="http://www.w3.org/ns/xproc" exclude-inline-prefixes="#all"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ex="extensions"
    xmlns:cx="http://xmlcalabash.com/ns/extensions" xmlns:c="http://www.w3.org/ns/xproc-step"
    version="3.0">
    
    <p:input port="source" primary="true" content-types="xml"
        href="movies.xml" sequence="false"/>
    
    <p:output port="result" primary="true" sequence="true"/>
    
    <p:validate-with-relax-ng name="validate">
        <p:with-input port="schema" href="xproc.rng"/>
    </p:validate-with-relax-ng>
    
    <p:unwrap match="films"/>
    <p:delete match="runtime//text()"/>
</p:declare-step>