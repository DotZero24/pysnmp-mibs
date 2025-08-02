_W='productNamingPlatformsVer1'
_V='productNamingLE46VM'
_U='productNamingLP24'
_T='productNamingLP16'
_S='productNaming4124'
_R='productNaming4116'
_Q='productNaming4108'
_P='productNaming4104Plus'
_O='productNaming4104'
_N='productNaming4102'
_M='productNaming0102'
_L='productNamingLiaison522'
_K='productNamingLiaison512'
_J='productNaming2102'
_I='productNaming1204'
_H='productNaming1124'
_G='productNaming1104'
_F='productNaming1102'
_E='productNamingPlatformName'
_D='MX-PRODUCT-NAMING-MIB'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixProducts,=mibBuilder.importSymbols('MX-SMI','mediatrixProducts')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
productNamingMIB=ModuleIdentity((1,3,6,1,4,1,4935,1,1000))
if mibBuilder.loadTexts:productNamingMIB.setRevisions(('2011-06-28 00:00','2009-10-01 00:00','2008-08-12 00:00','2008-06-17 00:00','2007-12-11 00:00','2007-03-21 00:00','2007-01-08 00:00','2005-06-23 00:00','2005-04-15 00:00','2004-02-02 00:00','2003-02-25 00:00'))
_ProductNamingMIBObjects_ObjectIdentity=ObjectIdentity
productNamingMIBObjects=_ProductNamingMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1,1000,1))
class _ProductNamingPlatformName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProductNamingPlatformName_Type.__name__=_B
_ProductNamingPlatformName_Object=MibScalar
productNamingPlatformName=_ProductNamingPlatformName_Object((1,3,6,1,4,1,4935,1,1000,1,15),_ProductNamingPlatformName_Type())
productNamingPlatformName.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingPlatformName.setStatus(_A)
_ProductNamingPlatforms_ObjectIdentity=ObjectIdentity
productNamingPlatforms=_ProductNamingPlatforms_ObjectIdentity((1,3,6,1,4,1,4935,1,1000,1,20))
class _ProductNaming1102_Type(OctetString):defaultValue=OctetString('Mediatrix 1102');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming1102_Type.__name__=_B
_ProductNaming1102_Object=MibScalar
productNaming1102=_ProductNaming1102_Object((1,3,6,1,4,1,4935,1,1000,1,20,5),_ProductNaming1102_Type())
productNaming1102.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming1102.setStatus(_A)
class _ProductNaming1104_Type(OctetString):defaultValue=OctetString('Mediatrix 1104');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming1104_Type.__name__=_B
_ProductNaming1104_Object=MibScalar
productNaming1104=_ProductNaming1104_Object((1,3,6,1,4,1,4935,1,1000,1,20,10),_ProductNaming1104_Type())
productNaming1104.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming1104.setStatus(_A)
class _ProductNaming1124_Type(OctetString):defaultValue=OctetString('Mediatrix 1124');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming1124_Type.__name__=_B
_ProductNaming1124_Object=MibScalar
productNaming1124=_ProductNaming1124_Object((1,3,6,1,4,1,4935,1,1000,1,20,15),_ProductNaming1124_Type())
productNaming1124.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming1124.setStatus(_A)
class _ProductNaming1204_Type(OctetString):defaultValue=OctetString('Mediatrix 1204');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming1204_Type.__name__=_B
_ProductNaming1204_Object=MibScalar
productNaming1204=_ProductNaming1204_Object((1,3,6,1,4,1,4935,1,1000,1,20,20),_ProductNaming1204_Type())
productNaming1204.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming1204.setStatus(_A)
class _ProductNaming2102_Type(OctetString):defaultValue=OctetString('Mediatrix 2102');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming2102_Type.__name__=_B
_ProductNaming2102_Object=MibScalar
productNaming2102=_ProductNaming2102_Object((1,3,6,1,4,1,4935,1,1000,1,20,25),_ProductNaming2102_Type())
productNaming2102.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming2102.setStatus(_A)
class _ProductNamingLiaison312_Type(OctetString):defaultValue=OctetString('Mediatrix Liaison 312');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLiaison312_Type.__name__=_B
_ProductNamingLiaison312_Object=MibScalar
productNamingLiaison312=_ProductNamingLiaison312_Object((1,3,6,1,4,1,4935,1,1000,1,20,30),_ProductNamingLiaison312_Type())
productNamingLiaison312.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLiaison312.setStatus(_A)
class _ProductNamingLiaison322_Type(OctetString):defaultValue=OctetString('Mediatrix Liaison 322');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLiaison322_Type.__name__=_B
_ProductNamingLiaison322_Object=MibScalar
productNamingLiaison322=_ProductNamingLiaison322_Object((1,3,6,1,4,1,4935,1,1000,1,20,35),_ProductNamingLiaison322_Type())
productNamingLiaison322.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLiaison322.setStatus(_A)
class _ProductNamingLiaison512_Type(OctetString):defaultValue=OctetString('Mediatrix Liaison 512');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLiaison512_Type.__name__=_B
_ProductNamingLiaison512_Object=MibScalar
productNamingLiaison512=_ProductNamingLiaison512_Object((1,3,6,1,4,1,4935,1,1000,1,20,75),_ProductNamingLiaison512_Type())
productNamingLiaison512.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLiaison512.setStatus(_A)
class _ProductNamingLiaison522_Type(OctetString):defaultValue=OctetString('Mediatrix Liaison 522');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLiaison522_Type.__name__=_B
_ProductNamingLiaison522_Object=MibScalar
productNamingLiaison522=_ProductNamingLiaison522_Object((1,3,6,1,4,1,4935,1,1000,1,20,80),_ProductNamingLiaison522_Type())
productNamingLiaison522.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLiaison522.setStatus(_A)
class _ProductNaming0102_Type(OctetString):defaultValue=OctetString('Mediatrix 0102');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming0102_Type.__name__=_B
_ProductNaming0102_Object=MibScalar
productNaming0102=_ProductNaming0102_Object((1,3,6,1,4,1,4935,1,1000,1,20,83),_ProductNaming0102_Type())
productNaming0102.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming0102.setStatus(_A)
class _ProductNaming4102_Type(OctetString):defaultValue=OctetString('Mediatrix 4102');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4102_Type.__name__=_B
_ProductNaming4102_Object=MibScalar
productNaming4102=_ProductNaming4102_Object((1,3,6,1,4,1,4935,1,1000,1,20,84),_ProductNaming4102_Type())
productNaming4102.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4102.setStatus(_A)
class _ProductNaming4104_Type(OctetString):defaultValue=OctetString('Mediatrix 4104');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4104_Type.__name__=_B
_ProductNaming4104_Object=MibScalar
productNaming4104=_ProductNaming4104_Object((1,3,6,1,4,1,4935,1,1000,1,20,85),_ProductNaming4104_Type())
productNaming4104.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4104.setStatus(_A)
class _ProductNaming4104Plus_Type(OctetString):defaultValue=OctetString('Mediatrix 4104plus');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4104Plus_Type.__name__=_B
_ProductNaming4104Plus_Object=MibScalar
productNaming4104Plus=_ProductNaming4104Plus_Object((1,3,6,1,4,1,4935,1,1000,1,20,88),_ProductNaming4104Plus_Type())
productNaming4104Plus.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4104Plus.setStatus(_A)
class _ProductNaming4108_Type(OctetString):defaultValue=OctetString('Mediatrix 4108');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4108_Type.__name__=_B
_ProductNaming4108_Object=MibScalar
productNaming4108=_ProductNaming4108_Object((1,3,6,1,4,1,4935,1,1000,1,20,90),_ProductNaming4108_Type())
productNaming4108.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4108.setStatus(_A)
class _ProductNaming4116_Type(OctetString):defaultValue=OctetString('Mediatrix 4116');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4116_Type.__name__=_B
_ProductNaming4116_Object=MibScalar
productNaming4116=_ProductNaming4116_Object((1,3,6,1,4,1,4935,1,1000,1,20,95),_ProductNaming4116_Type())
productNaming4116.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4116.setStatus(_A)
class _ProductNaming4124_Type(OctetString):defaultValue=OctetString('Mediatrix 4124');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNaming4124_Type.__name__=_B
_ProductNaming4124_Object=MibScalar
productNaming4124=_ProductNaming4124_Object((1,3,6,1,4,1,4935,1,1000,1,20,100),_ProductNaming4124_Type())
productNaming4124.setMaxAccess(_C)
if mibBuilder.loadTexts:productNaming4124.setStatus(_A)
class _ProductNamingLP16_Type(OctetString):defaultValue=OctetString('Mediatrix LP16');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLP16_Type.__name__=_B
_ProductNamingLP16_Object=MibScalar
productNamingLP16=_ProductNamingLP16_Object((1,3,6,1,4,1,4935,1,1000,1,20,105),_ProductNamingLP16_Type())
productNamingLP16.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLP16.setStatus(_A)
class _ProductNamingLP24_Type(OctetString):defaultValue=OctetString('Mediatrix LP24');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLP24_Type.__name__=_B
_ProductNamingLP24_Object=MibScalar
productNamingLP24=_ProductNamingLP24_Object((1,3,6,1,4,1,4935,1,1000,1,20,110),_ProductNamingLP24_Type())
productNamingLP24.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLP24.setStatus(_A)
class _ProductNamingLE46VM_Type(OctetString):defaultValue=OctetString('Ciena LE46 VM');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ProductNamingLE46VM_Type.__name__=_B
_ProductNamingLE46VM_Object=MibScalar
productNamingLE46VM=_ProductNamingLE46VM_Object((1,3,6,1,4,1,4935,1,1000,1,20,120),_ProductNamingLE46VM_Type())
productNamingLE46VM.setMaxAccess(_C)
if mibBuilder.loadTexts:productNamingLE46VM.setStatus(_A)
_ProductNamingConformance_ObjectIdentity=ObjectIdentity
productNamingConformance=_ProductNamingConformance_ObjectIdentity((1,3,6,1,4,1,4935,1,1000,5))
_ProductNamingCompliances_ObjectIdentity=ObjectIdentity
productNamingCompliances=_ProductNamingCompliances_ObjectIdentity((1,3,6,1,4,1,4935,1,1000,5,1))
_ProductNamingGroups_ObjectIdentity=ObjectIdentity
productNamingGroups=_ProductNamingGroups_ObjectIdentity((1,3,6,1,4,1,4935,1,1000,5,5))
productNamingPlatformsVer1=ObjectGroup((1,3,6,1,4,1,4935,1,1000,5,5,10))
productNamingPlatformsVer1.setObjects(*((_D,_E),(_D,_F),(_D,_G),(_D,_H),(_D,_I),(_D,_J),(_D,_K),(_D,_L),(_D,_M),(_D,_N),(_D,_O),(_D,_P),(_D,_Q),(_D,_R),(_D,_S),(_D,_T),(_D,_U),(_D,_V)))
if mibBuilder.loadTexts:productNamingPlatformsVer1.setStatus(_A)
productNamingComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,1,1000,5,1,1))
productNamingComplVer1.setObjects((_D,_W))
if mibBuilder.loadTexts:productNamingComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'productNamingMIB':productNamingMIB,'productNamingMIBObjects':productNamingMIBObjects,_E:productNamingPlatformName,'productNamingPlatforms':productNamingPlatforms,_F:productNaming1102,_G:productNaming1104,_H:productNaming1124,_I:productNaming1204,_J:productNaming2102,'productNamingLiaison312':productNamingLiaison312,'productNamingLiaison322':productNamingLiaison322,_K:productNamingLiaison512,_L:productNamingLiaison522,_M:productNaming0102,_N:productNaming4102,_O:productNaming4104,_P:productNaming4104Plus,_Q:productNaming4108,_R:productNaming4116,_S:productNaming4124,_T:productNamingLP16,_U:productNamingLP24,_V:productNamingLE46VM,'productNamingConformance':productNamingConformance,'productNamingCompliances':productNamingCompliances,'productNamingComplVer1':productNamingComplVer1,'productNamingGroups':productNamingGroups,_W:productNamingPlatformsVer1})