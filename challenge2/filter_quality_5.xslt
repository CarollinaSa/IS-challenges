<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" indent="yes"/>

  <!-- Template for the root element -->
  <xsl:template match="/WineData">
    <WineData>
      <!-- Filter wines with quality equal to 5 -->
      <xsl:for-each select="Wine[quality='5']">
        <xsl:copy-of select="."/>
      </xsl:for-each>
    </WineData>
  </xsl:template>

</xsl:stylesheet>
