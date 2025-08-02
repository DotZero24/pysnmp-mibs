_E='read-write'
_D='Integer32'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fcSwitch,=mibBuilder.importSymbols('Brocade-REG-MIB','fcSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bcCustomOperation=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,52))
if mibBuilder.loadTexts:bcCustomOperation.setRevisions(('2011-12-19 10:30',))
_HwinfospsaveCmd_ObjectIdentity=ObjectIdentity
hwinfospsaveCmd=_HwinfospsaveCmd_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,52,1))
if mibBuilder.loadTexts:hwinfospsaveCmd.setStatus(_A)
class _HwinfospsaveSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HwinfospsaveSet_Type.__name__=_B
_HwinfospsaveSet_Object=MibScalar
hwinfospsaveSet=_HwinfospsaveSet_Object((1,3,6,1,4,1,1588,2,1,1,52,1,1),_HwinfospsaveSet_Type())
hwinfospsaveSet.setMaxAccess(_E)
if mibBuilder.loadTexts:hwinfospsaveSet.setStatus(_A)
class _HwinfospsaveGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('success',0),('ftperror',1),('progressing',2),('systemerror',3)))
_HwinfospsaveGet_Type.__name__=_D
_HwinfospsaveGet_Object=MibScalar
hwinfospsaveGet=_HwinfospsaveGet_Object((1,3,6,1,4,1,1588,2,1,1,52,1,2),_HwinfospsaveGet_Type())
hwinfospsaveGet.setMaxAccess(_C)
if mibBuilder.loadTexts:hwinfospsaveGet.setStatus(_A)
_HwUpdateFilecmd_ObjectIdentity=ObjectIdentity
hwUpdateFilecmd=_HwUpdateFilecmd_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,52,2))
if mibBuilder.loadTexts:hwUpdateFilecmd.setStatus(_A)
class _HwUpdateFile_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HwUpdateFile_Type.__name__=_B
_HwUpdateFile_Object=MibScalar
hwUpdateFile=_HwUpdateFile_Object((1,3,6,1,4,1,1588,2,1,1,52,2,1),_HwUpdateFile_Type())
hwUpdateFile.setMaxAccess(_E)
if mibBuilder.loadTexts:hwUpdateFile.setStatus(_A)
class _HwUpdateFileInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HwUpdateFileInfo_Type.__name__=_B
_HwUpdateFileInfo_Object=MibScalar
hwUpdateFileInfo=_HwUpdateFileInfo_Object((1,3,6,1,4,1,1588,2,1,1,52,2,2),_HwUpdateFileInfo_Type())
hwUpdateFileInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUpdateFileInfo.setStatus(_A)
class _HwSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_HwSoftwareVersion_Type.__name__=_B
_HwSoftwareVersion_Object=MibScalar
hwSoftwareVersion=_HwSoftwareVersion_Object((1,3,6,1,4,1,1588,2,1,1,52,2,3),_HwSoftwareVersion_Type())
hwSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSoftwareVersion.setStatus(_A)
mibBuilder.exportSymbols('BCCUSTOM-OPR-MIB',**{'bcCustomOperation':bcCustomOperation,'hwinfospsaveCmd':hwinfospsaveCmd,'hwinfospsaveSet':hwinfospsaveSet,'hwinfospsaveGet':hwinfospsaveGet,'hwUpdateFilecmd':hwUpdateFilecmd,'hwUpdateFile':hwUpdateFile,'hwUpdateFileInfo':hwUpdateFileInfo,'hwSoftwareVersion':hwSoftwareVersion})