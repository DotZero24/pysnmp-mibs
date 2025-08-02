_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mellanoxProducts,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxProductsMib=ModuleIdentity((1,3,6,1,4,1,33049,1,1))
if mibBuilder.loadTexts:mellanoxProductsMib.setRevisions(('2020-08-26 00:00',))
_SwitchXFamily_ObjectIdentity=ObjectIdentity
switchXFamily=_SwitchXFamily_ObjectIdentity((1,3,6,1,4,1,33049,1,1,1))
_Sx1012_Type=ObjectIdentifier
_Sx1012_Object=MibScalar
sx1012=_Sx1012_Object((1,3,6,1,4,1,33049,1,1,1,1012),_Sx1012_Type())
sx1012.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1012.setStatus(_B)
_Sx1016_Type=ObjectIdentifier
_Sx1016_Object=MibScalar
sx1016=_Sx1016_Object((1,3,6,1,4,1,33049,1,1,1,1016),_Sx1016_Type())
sx1016.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1016.setStatus(_B)
_Sx1024_Type=ObjectIdentifier
_Sx1024_Object=MibScalar
sx1024=_Sx1024_Object((1,3,6,1,4,1,33049,1,1,1,1024),_Sx1024_Type())
sx1024.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1024.setStatus(_B)
_Sx1035_Type=ObjectIdentifier
_Sx1035_Object=MibScalar
sx1035=_Sx1035_Object((1,3,6,1,4,1,33049,1,1,1,1035),_Sx1035_Type())
sx1035.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1035.setStatus(_B)
_Sx1036_Type=ObjectIdentifier
_Sx1036_Object=MibScalar
sx1036=_Sx1036_Object((1,3,6,1,4,1,33049,1,1,1,1036),_Sx1036_Type())
sx1036.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1036.setStatus(_B)
_Sx1400_Type=ObjectIdentifier
_Sx1400_Object=MibScalar
sx1400=_Sx1400_Object((1,3,6,1,4,1,33049,1,1,1,1400),_Sx1400_Type())
sx1400.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1400.setStatus(_B)
_Msx1410_Type=ObjectIdentifier
_Msx1410_Object=MibScalar
msx1410=_Msx1410_Object((1,3,6,1,4,1,33049,1,1,1,1410),_Msx1410_Type())
msx1410.setMaxAccess(_A)
if mibBuilder.loadTexts:msx1410.setStatus(_B)
_Sx1700_Type=ObjectIdentifier
_Sx1700_Object=MibScalar
sx1700=_Sx1700_Object((1,3,6,1,4,1,33049,1,1,1,1700),_Sx1700_Type())
sx1700.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1700.setStatus(_B)
_Sx1710_Type=ObjectIdentifier
_Sx1710_Object=MibScalar
sx1710=_Sx1710_Object((1,3,6,1,4,1,33049,1,1,1,1710),_Sx1710_Type())
sx1710.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1710.setStatus(_B)
_Sn2010_Type=ObjectIdentifier
_Sn2010_Object=MibScalar
sn2010=_Sn2010_Object((1,3,6,1,4,1,33049,1,1,1,2010),_Sn2010_Type())
sn2010.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2010.setStatus(_B)
_Sn2100_Type=ObjectIdentifier
_Sn2100_Object=MibScalar
sn2100=_Sn2100_Object((1,3,6,1,4,1,33049,1,1,1,2100),_Sn2100_Type())
sn2100.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2100.setStatus(_B)
_Sn2100b_Type=ObjectIdentifier
_Sn2100b_Object=MibScalar
sn2100b=_Sn2100b_Object((1,3,6,1,4,1,33049,1,1,1,2101),_Sn2100b_Type())
sn2100b.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2100b.setStatus(_B)
_Sn2410_Type=ObjectIdentifier
_Sn2410_Object=MibScalar
sn2410=_Sn2410_Object((1,3,6,1,4,1,33049,1,1,1,2410),_Sn2410_Type())
sn2410.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2410.setStatus(_B)
_Sn2700_Type=ObjectIdentifier
_Sn2700_Object=MibScalar
sn2700=_Sn2700_Object((1,3,6,1,4,1,33049,1,1,1,2700),_Sn2700_Type())
sn2700.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2700.setStatus(_B)
_Sn2700b_Type=ObjectIdentifier
_Sn2700b_Object=MibScalar
sn2700b=_Sn2700b_Object((1,3,6,1,4,1,33049,1,1,1,2701),_Sn2700b_Type())
sn2700b.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2700b.setStatus(_B)
_Sn2740_Type=ObjectIdentifier
_Sn2740_Object=MibScalar
sn2740=_Sn2740_Object((1,3,6,1,4,1,33049,1,1,1,2740),_Sn2740_Type())
sn2740.setMaxAccess(_A)
if mibBuilder.loadTexts:sn2740.setStatus(_B)
_Sn3420_Type=ObjectIdentifier
_Sn3420_Object=MibScalar
sn3420=_Sn3420_Object((1,3,6,1,4,1,33049,1,1,1,3420),_Sn3420_Type())
sn3420.setMaxAccess(_A)
if mibBuilder.loadTexts:sn3420.setStatus(_B)
_Sn3700_Type=ObjectIdentifier
_Sn3700_Object=MibScalar
sn3700=_Sn3700_Object((1,3,6,1,4,1,33049,1,1,1,3700),_Sn3700_Type())
sn3700.setMaxAccess(_A)
if mibBuilder.loadTexts:sn3700.setStatus(_B)
_Sn3800_Type=ObjectIdentifier
_Sn3800_Object=MibScalar
sn3800=_Sn3800_Object((1,3,6,1,4,1,33049,1,1,1,3800),_Sn3800_Type())
sn3800.setMaxAccess(_A)
if mibBuilder.loadTexts:sn3800.setStatus(_B)
_Sn4600_Type=ObjectIdentifier
_Sn4600_Object=MibScalar
sn4600=_Sn4600_Object((1,3,6,1,4,1,33049,1,1,1,4600),_Sn4600_Type())
sn4600.setMaxAccess(_A)
if mibBuilder.loadTexts:sn4600.setStatus(_B)
_Sn4700_Type=ObjectIdentifier
_Sn4700_Object=MibScalar
sn4700=_Sn4700_Object((1,3,6,1,4,1,33049,1,1,1,4700),_Sn4700_Type())
sn4700.setMaxAccess(_A)
if mibBuilder.loadTexts:sn4700.setStatus(_B)
_Mtx6000_Type=ObjectIdentifier
_Mtx6000_Object=MibScalar
mtx6000=_Mtx6000_Object((1,3,6,1,4,1,33049,1,1,1,6000),_Mtx6000_Type())
mtx6000.setMaxAccess(_A)
if mibBuilder.loadTexts:mtx6000.setStatus(_B)
_Sx6012_Type=ObjectIdentifier
_Sx6012_Object=MibScalar
sx6012=_Sx6012_Object((1,3,6,1,4,1,33049,1,1,1,6012),_Sx6012_Type())
sx6012.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6012.setStatus(_B)
_Sx6018_Type=ObjectIdentifier
_Sx6018_Object=MibScalar
sx6018=_Sx6018_Object((1,3,6,1,4,1,33049,1,1,1,6018),_Sx6018_Type())
sx6018.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6018.setStatus(_B)
_Sx6036_Type=ObjectIdentifier
_Sx6036_Object=MibScalar
sx6036=_Sx6036_Object((1,3,6,1,4,1,33049,1,1,1,6036),_Sx6036_Type())
sx6036.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6036.setStatus(_B)
_Mtx6100_Type=ObjectIdentifier
_Mtx6100_Object=MibScalar
mtx6100=_Mtx6100_Object((1,3,6,1,4,1,33049,1,1,1,6100),_Mtx6100_Type())
mtx6100.setMaxAccess(_A)
if mibBuilder.loadTexts:mtx6100.setStatus(_B)
_Mtx6240_Type=ObjectIdentifier
_Mtx6240_Object=MibScalar
mtx6240=_Mtx6240_Object((1,3,6,1,4,1,33049,1,1,1,6240),_Mtx6240_Type())
mtx6240.setMaxAccess(_A)
if mibBuilder.loadTexts:mtx6240.setStatus(_B)
_Mtx6280_Type=ObjectIdentifier
_Mtx6280_Object=MibScalar
mtx6280=_Mtx6280_Object((1,3,6,1,4,1,33049,1,1,1,6280),_Mtx6280_Type())
mtx6280.setMaxAccess(_A)
if mibBuilder.loadTexts:mtx6280.setStatus(_B)
_Sx6506_Type=ObjectIdentifier
_Sx6506_Object=MibScalar
sx6506=_Sx6506_Object((1,3,6,1,4,1,33049,1,1,1,6506),_Sx6506_Type())
sx6506.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6506.setStatus(_B)
_Sx6512_Type=ObjectIdentifier
_Sx6512_Object=MibScalar
sx6512=_Sx6512_Object((1,3,6,1,4,1,33049,1,1,1,6512),_Sx6512_Type())
sx6512.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6512.setStatus(_B)
_Sx6518_Type=ObjectIdentifier
_Sx6518_Object=MibScalar
sx6518=_Sx6518_Object((1,3,6,1,4,1,33049,1,1,1,6518),_Sx6518_Type())
sx6518.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6518.setStatus(_B)
_Sx6536_Type=ObjectIdentifier
_Sx6536_Object=MibScalar
sx6536=_Sx6536_Object((1,3,6,1,4,1,33049,1,1,1,6536),_Sx6536_Type())
sx6536.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6536.setStatus(_B)
_Sx6700_Type=ObjectIdentifier
_Sx6700_Object=MibScalar
sx6700=_Sx6700_Object((1,3,6,1,4,1,33049,1,1,1,6700),_Sx6700_Type())
sx6700.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6700.setStatus(_B)
_Sx6710_Type=ObjectIdentifier
_Sx6710_Object=MibScalar
sx6710=_Sx6710_Object((1,3,6,1,4,1,33049,1,1,1,6710),_Sx6710_Type())
sx6710.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6710.setStatus(_B)
_Sx6720_Type=ObjectIdentifier
_Sx6720_Object=MibScalar
sx6720=_Sx6720_Object((1,3,6,1,4,1,33049,1,1,1,6720),_Sx6720_Type())
sx6720.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6720.setStatus(_B)
_Sx6730_Type=ObjectIdentifier
_Sx6730_Object=MibScalar
sx6730=_Sx6730_Object((1,3,6,1,4,1,33049,1,1,1,6730),_Sx6730_Type())
sx6730.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6730.setStatus(_B)
_Cs7500_Type=ObjectIdentifier
_Cs7500_Object=MibScalar
cs7500=_Cs7500_Object((1,3,6,1,4,1,33049,1,1,1,7500),_Cs7500_Type())
cs7500.setMaxAccess(_A)
if mibBuilder.loadTexts:cs7500.setStatus(_B)
_Cs7510_Type=ObjectIdentifier
_Cs7510_Object=MibScalar
cs7510=_Cs7510_Object((1,3,6,1,4,1,33049,1,1,1,7510),_Cs7510_Type())
cs7510.setMaxAccess(_A)
if mibBuilder.loadTexts:cs7510.setStatus(_B)
_Cs7520_Type=ObjectIdentifier
_Cs7520_Object=MibScalar
cs7520=_Cs7520_Object((1,3,6,1,4,1,33049,1,1,1,7520),_Cs7520_Type())
cs7520.setMaxAccess(_A)
if mibBuilder.loadTexts:cs7520.setStatus(_B)
_Sb7700_Type=ObjectIdentifier
_Sb7700_Object=MibScalar
sb7700=_Sb7700_Object((1,3,6,1,4,1,33049,1,1,1,7700),_Sb7700_Type())
sb7700.setMaxAccess(_A)
if mibBuilder.loadTexts:sb7700.setStatus(_B)
_Sb7780_Type=ObjectIdentifier
_Sb7780_Object=MibScalar
sb7780=_Sb7780_Object((1,3,6,1,4,1,33049,1,1,1,7780),_Sb7780_Type())
sb7780.setMaxAccess(_A)
if mibBuilder.loadTexts:sb7780.setStatus(_B)
_Sb7800_Type=ObjectIdentifier
_Sb7800_Object=MibScalar
sb7800=_Sb7800_Object((1,3,6,1,4,1,33049,1,1,1,7800),_Sb7800_Type())
sb7800.setMaxAccess(_A)
if mibBuilder.loadTexts:sb7800.setStatus(_B)
_Sb7880_Type=ObjectIdentifier
_Sb7880_Object=MibScalar
sb7880=_Sb7880_Object((1,3,6,1,4,1,33049,1,1,1,7880),_Sb7880_Type())
sb7880.setMaxAccess(_A)
if mibBuilder.loadTexts:sb7880.setStatus(_B)
_Mtq8100_Type=ObjectIdentifier
_Mtq8100_Object=MibScalar
mtq8100=_Mtq8100_Object((1,3,6,1,4,1,33049,1,1,1,8100),_Mtq8100_Type())
mtq8100.setMaxAccess(_A)
if mibBuilder.loadTexts:mtq8100.setStatus(_B)
_Mtq8200_Type=ObjectIdentifier
_Mtq8200_Object=MibScalar
mtq8200=_Mtq8200_Object((1,3,6,1,4,1,33049,1,1,1,8200),_Mtq8200_Type())
mtq8200.setMaxAccess(_A)
if mibBuilder.loadTexts:mtq8200.setStatus(_B)
_Cs8500_Type=ObjectIdentifier
_Cs8500_Object=MibScalar
cs8500=_Cs8500_Object((1,3,6,1,4,1,33049,1,1,1,8500),_Cs8500_Type())
cs8500.setMaxAccess(_A)
if mibBuilder.loadTexts:cs8500.setStatus(_B)
_Mqm8700_Type=ObjectIdentifier
_Mqm8700_Object=MibScalar
mqm8700=_Mqm8700_Object((1,3,6,1,4,1,33049,1,1,1,8700),_Mqm8700_Type())
mqm8700.setMaxAccess(_A)
if mibBuilder.loadTexts:mqm8700.setStatus(_B)
_Sx1012x_Type=ObjectIdentifier
_Sx1012x_Object=MibScalar
sx1012x=_Sx1012x_Object((1,3,6,1,4,1,33049,1,1,1,10121),_Sx1012x_Type())
sx1012x.setMaxAccess(_A)
if mibBuilder.loadTexts:sx1012x.setStatus(_B)
_Sn27002_Type=ObjectIdentifier
_Sn27002_Object=MibScalar
sn27002=_Sn27002_Object((1,3,6,1,4,1,33049,1,1,1,27002),_Sn27002_Type())
sn27002.setMaxAccess(_A)
if mibBuilder.loadTexts:sn27002.setStatus(_B)
_Sx6018g_Type=ObjectIdentifier
_Sx6018g_Object=MibScalar
sx6018g=_Sx6018g_Object((1,3,6,1,4,1,33049,1,1,1,60181),_Sx6018g_Type())
sx6018g.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6018g.setStatus(_B)
_Sx6036g_Type=ObjectIdentifier
_Sx6036g_Object=MibScalar
sx6036g=_Sx6036g_Object((1,3,6,1,4,1,33049,1,1,1,60361),_Sx6036g_Type())
sx6036g.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6036g.setStatus(_B)
_Sx6710g_Type=ObjectIdentifier
_Sx6710g_Object=MibScalar
sx6710g=_Sx6710g_Object((1,3,6,1,4,1,33049,1,1,1,67101),_Sx6710g_Type())
sx6710g.setMaxAccess(_A)
if mibBuilder.loadTexts:sx6710g.setStatus(_B)
_Sn3700c_Type=ObjectIdentifier
_Sn3700c_Object=MibScalar
sn3700c=_Sn3700c_Object((1,3,6,1,4,1,33049,1,1,1,370013),_Sn3700c_Type())
sn3700c.setMaxAccess(_A)
if mibBuilder.loadTexts:sn3700c.setStatus(_B)
_Sn4600c_Type=ObjectIdentifier
_Sn4600c_Object=MibScalar
sn4600c=_Sn4600c_Object((1,3,6,1,4,1,33049,1,1,1,460013),_Sn4600c_Type())
sn4600c.setMaxAccess(_A)
if mibBuilder.loadTexts:sn4600c.setStatus(_B)
_Ufm_ObjectIdentity=ObjectIdentity
ufm=_Ufm_ObjectIdentity((1,3,6,1,4,1,33049,1,1,2))
_UfmAppliance_Type=Integer32
_UfmAppliance_Object=MibScalar
ufmAppliance=_UfmAppliance_Object((1,3,6,1,4,1,33049,1,1,2,1),_UfmAppliance_Type())
ufmAppliance.setMaxAccess(_A)
if mibBuilder.loadTexts:ufmAppliance.setStatus(_B)
_UfmServer_Type=Integer32
_UfmServer_Object=MibScalar
ufmServer=_UfmServer_Object((1,3,6,1,4,1,33049,1,1,2,2),_UfmServer_Type())
ufmServer.setMaxAccess(_A)
if mibBuilder.loadTexts:ufmServer.setStatus(_B)
_Neo_ObjectIdentity=ObjectIdentity
neo=_Neo_ObjectIdentity((1,3,6,1,4,1,33049,1,1,3))
_NeoAppliance_Type=Integer32
_NeoAppliance_Object=MibScalar
neoAppliance=_NeoAppliance_Object((1,3,6,1,4,1,33049,1,1,3,1),_NeoAppliance_Type())
neoAppliance.setMaxAccess(_A)
if mibBuilder.loadTexts:neoAppliance.setStatus(_B)
mibBuilder.exportSymbols('MELLANOX-PRODUCTS-MIB',**{'mellanoxProductsMib':mellanoxProductsMib,'switchXFamily':switchXFamily,'sx1012':sx1012,'sx1016':sx1016,'sx1024':sx1024,'sx1035':sx1035,'sx1036':sx1036,'sx1400':sx1400,'msx1410':msx1410,'sx1700':sx1700,'sx1710':sx1710,'sn2010':sn2010,'sn2100':sn2100,'sn2100b':sn2100b,'sn2410':sn2410,'sn2700':sn2700,'sn2700b':sn2700b,'sn2740':sn2740,'sn3420':sn3420,'sn3700':sn3700,'sn3800':sn3800,'sn4600':sn4600,'sn4700':sn4700,'mtx6000':mtx6000,'sx6012':sx6012,'sx6018':sx6018,'sx6036':sx6036,'mtx6100':mtx6100,'mtx6240':mtx6240,'mtx6280':mtx6280,'sx6506':sx6506,'sx6512':sx6512,'sx6518':sx6518,'sx6536':sx6536,'sx6700':sx6700,'sx6710':sx6710,'sx6720':sx6720,'sx6730':sx6730,'cs7500':cs7500,'cs7510':cs7510,'cs7520':cs7520,'sb7700':sb7700,'sb7780':sb7780,'sb7800':sb7800,'sb7880':sb7880,'mtq8100':mtq8100,'mtq8200':mtq8200,'cs8500':cs8500,'mqm8700':mqm8700,'sx1012x':sx1012x,'sn27002':sn27002,'sx6018g':sx6018g,'sx6036g':sx6036g,'sx6710g':sx6710g,'sn3700c':sn3700c,'sn4600c':sn4600c,'ufm':ufm,'ufmAppliance':ufmAppliance,'ufmServer':ufmServer,'neo':neo,'neoAppliance':neoAppliance})