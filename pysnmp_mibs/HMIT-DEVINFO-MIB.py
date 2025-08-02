_F='hmITDevIndex'
_E='HMIT-DEVINFO-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITMgmt,=mibBuilder.importSymbols('HMIT-SMI','hmITMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
hmITDeviceInfoMib=ModuleIdentity((1,3,6,1,4,1,248,100,1,3,602))
if mibBuilder.loadTexts:hmITDeviceInfoMib.setRevisions(('2010-01-08 17:00',))
_HmITDeviceInformation_ObjectIdentity=ObjectIdentity
hmITDeviceInformation=_HmITDeviceInformation_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,602,1))
_HmITDeviceSerialNumber_Type=DisplayString
_HmITDeviceSerialNumber_Object=MibScalar
hmITDeviceSerialNumber=_HmITDeviceSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,602,1,1),_HmITDeviceSerialNumber_Type())
hmITDeviceSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDeviceSerialNumber.setStatus(_A)
class _HmITDevHwModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HmITDevHwModel_Type.__name__=_C
_HmITDevHwModel_Object=MibScalar
hmITDevHwModel=_HmITDevHwModel_Object((1,3,6,1,4,1,248,100,1,3,602,1,2),_HmITDevHwModel_Type())
hmITDevHwModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevHwModel.setStatus(_A)
_HmITDeviceInfoTable_Object=MibTable
hmITDeviceInfoTable=_HmITDeviceInfoTable_Object((1,3,6,1,4,1,248,100,1,3,602,1,100))
if mibBuilder.loadTexts:hmITDeviceInfoTable.setStatus(_A)
_HmITDeviceInfoEntry_Object=MibTableRow
hmITDeviceInfoEntry=_HmITDeviceInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1))
hmITDeviceInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hmITDeviceInfoEntry.setStatus(_A)
class _HmITDevIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITDevIndex_Type.__name__=_D
_HmITDevIndex_Object=MibTableColumn
hmITDevIndex=_HmITDevIndex_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,1),_HmITDevIndex_Type())
hmITDevIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmITDevIndex.setStatus(_A)
_HmITDevName_Type=DisplayString
_HmITDevName_Object=MibTableColumn
hmITDevName=_HmITDevName_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,2),_HmITDevName_Type())
hmITDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevName.setStatus(_A)
_HmITDevType_Type=Unsigned32
_HmITDevType_Object=MibTableColumn
hmITDevType=_HmITDevType_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,3),_HmITDevType_Type())
hmITDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevType.setStatus(_A)
_HmITDevHwSerial_Type=DisplayString
_HmITDevHwSerial_Object=MibTableColumn
hmITDevHwSerial=_HmITDevHwSerial_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,4),_HmITDevHwSerial_Type())
hmITDevHwSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevHwSerial.setStatus(_A)
_HmITDevHwVersion_Type=DisplayString
_HmITDevHwVersion_Object=MibTableColumn
hmITDevHwVersion=_HmITDevHwVersion_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,5),_HmITDevHwVersion_Type())
hmITDevHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevHwVersion.setStatus(_A)
_HmITDevSwVersion_Type=DisplayString
_HmITDevSwVersion_Object=MibTableColumn
hmITDevSwVersion=_HmITDevSwVersion_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,6),_HmITDevSwVersion_Type())
hmITDevSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevSwVersion.setStatus(_A)
class _HmITDevCfgVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmITDevCfgVersion_Type.__name__=_C
_HmITDevCfgVersion_Object=MibTableColumn
hmITDevCfgVersion=_HmITDevCfgVersion_Object((1,3,6,1,4,1,248,100,1,3,602,1,100,1,7),_HmITDevCfgVersion_Type())
hmITDevCfgVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITDevCfgVersion.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hmITDeviceInfoMib':hmITDeviceInfoMib,'hmITDeviceInformation':hmITDeviceInformation,'hmITDeviceSerialNumber':hmITDeviceSerialNumber,'hmITDevHwModel':hmITDevHwModel,'hmITDeviceInfoTable':hmITDeviceInfoTable,'hmITDeviceInfoEntry':hmITDeviceInfoEntry,_F:hmITDevIndex,'hmITDevName':hmITDevName,'hmITDevType':hmITDevType,'hmITDevHwSerial':hmITDevHwSerial,'hmITDevHwVersion':hmITDevHwVersion,'hmITDevSwVersion':hmITDevSwVersion,'hmITDevCfgVersion':hmITDevCfgVersion})