<?python
title="Result Page"
?>

<html xmlns="http://www.w3.org/xhtml"
      xmlns:py="http://purl.org/kid/ns#"
>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type" />
  <title py:content="title" />
</head>
<body>
<h1>Result Page</h1>
<table style="text-align: left; width: 437px;" border="1"
 cellpadding="2" cellspacing="2">
    <tbody>
      <tr>
        <td style="width: 202px;">Flowrate, BPH   </td>
        <td style="width: 218px;">$flowrate</td>
      </tr>
      <tr>
        <td style="width: 202px;">Expected Flowrate, BPH   </td>
        <td style="width: 218px;">$expected</td>
      </tr>
      <tr>
        <td style="width: 202px;">Product
(crude, refined product, water)
        </td>
        <td style="width: 218px;">$product</td>
      </tr>
      <tr>
        <td style="width: 202px;">Fluid
density, lb/ft3
        </td>
        <td style="width: 218px;">$density</td>
      </tr>
      <tr>
        <td style="width: 202px;">Viscosity, cP
        </td>
        <td style="width: 218px;">$viscosity</td>
      </tr>
      <tr>
        <td style="width: 202px;">Pipe
ID, inches
        </td>
        <td style="width: 218px;">$id</td>
      </tr>
      <tr>
        <td style="width: 202px;">Length, miles
        </td>
        <td style="width: 218px;">$length</td>
      </tr>
      <tr>
        <td style="width: 202px;">LP Required, ppm
        </td>
        <td style="width: 218px;"><strong>$ppm</strong></td>
      </tr>
    </tbody>
  </table>
</body>
</html>
