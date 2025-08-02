_J='h3cObjectInfoTableGroup'
_I='h3cObjectInfoValue'
_H='h3cObjectInfoTypeExtension'
_G='h3cObjectInfoType'
_F='h3cObjectInfoOID'
_E='Integer32'
_D='OctetString'
_C='not-accessible'
_B='H3C-OBJECT-INFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cObjectInfo=ModuleIdentity((1,3,6,1,4,1,2011,10,2,55))
if mibBuilder.loadTexts:h3cObjectInfo.setRevisions(('2004-12-27 00:00',))
_H3cObjectInformation_ObjectIdentity=ObjectIdentity
h3cObjectInformation=_H3cObjectInformation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,55,1))
_H3cObjectInfoTable_Object=MibTable
h3cObjectInfoTable=_H3cObjectInfoTable_Object((1,3,6,1,4,1,2011,10,2,55,1,1))
if mibBuilder.loadTexts:h3cObjectInfoTable.setStatus(_A)
_H3cObjectInfoEntry_Object=MibTableRow
h3cObjectInfoEntry=_H3cObjectInfoEntry_Object((1,3,6,1,4,1,2011,10,2,55,1,1,1))
h3cObjectInfoEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cObjectInfoEntry.setStatus(_A)
_H3cObjectInfoOID_Type=ObjectIdentifier
_H3cObjectInfoOID_Object=MibTableColumn
h3cObjectInfoOID=_H3cObjectInfoOID_Object((1,3,6,1,4,1,2011,10,2,55,1,1,1,1),_H3cObjectInfoOID_Type())
h3cObjectInfoOID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjectInfoOID.setStatus(_A)
class _H3cObjectInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('reserved',1),('accessType',2),('dataType',3),('dataRange',4),('dataLength',5)))
_H3cObjectInfoType_Type.__name__=_E
_H3cObjectInfoType_Object=MibTableColumn
h3cObjectInfoType=_H3cObjectInfoType_Object((1,3,6,1,4,1,2011,10,2,55,1,1,1,2),_H3cObjectInfoType_Type())
h3cObjectInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjectInfoType.setStatus(_A)
class _H3cObjectInfoTypeExtension_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cObjectInfoTypeExtension_Type.__name__=_D
_H3cObjectInfoTypeExtension_Object=MibTableColumn
h3cObjectInfoTypeExtension=_H3cObjectInfoTypeExtension_Object((1,3,6,1,4,1,2011,10,2,55,1,1,1,3),_H3cObjectInfoTypeExtension_Type())
h3cObjectInfoTypeExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cObjectInfoTypeExtension.setStatus(_A)
_H3cObjectInfoValue_Type=OctetString
_H3cObjectInfoValue_Object=MibTableColumn
h3cObjectInfoValue=_H3cObjectInfoValue_Object((1,3,6,1,4,1,2011,10,2,55,1,1,1,4),_H3cObjectInfoValue_Type())
h3cObjectInfoValue.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cObjectInfoValue.setStatus(_A)
_H3cObjectInfoMIBConformance_ObjectIdentity=ObjectIdentity
h3cObjectInfoMIBConformance=_H3cObjectInfoMIBConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,55,2))
_H3cObjectInfoMIBCompliances_ObjectIdentity=ObjectIdentity
h3cObjectInfoMIBCompliances=_H3cObjectInfoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,55,2,1))
_H3cObjectInfoMIBGroups_ObjectIdentity=ObjectIdentity
h3cObjectInfoMIBGroups=_H3cObjectInfoMIBGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,55,2,2))
h3cObjectInfoTableGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,55,2,2,1))
h3cObjectInfoTableGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:h3cObjectInfoTableGroup.setStatus(_A)
h3cObjectInfoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,55,2,1,1))
h3cObjectInfoMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:h3cObjectInfoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cObjectInfo':h3cObjectInfo,'h3cObjectInformation':h3cObjectInformation,'h3cObjectInfoTable':h3cObjectInfoTable,'h3cObjectInfoEntry':h3cObjectInfoEntry,_F:h3cObjectInfoOID,_G:h3cObjectInfoType,_H:h3cObjectInfoTypeExtension,_I:h3cObjectInfoValue,'h3cObjectInfoMIBConformance':h3cObjectInfoMIBConformance,'h3cObjectInfoMIBCompliances':h3cObjectInfoMIBCompliances,'h3cObjectInfoMIBCompliance':h3cObjectInfoMIBCompliance,'h3cObjectInfoMIBGroups':h3cObjectInfoMIBGroups,_J:h3cObjectInfoTableGroup})