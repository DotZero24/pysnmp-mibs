_J='hpnicfObjectInfoTableGroup'
_I='hpnicfObjectInfoValue'
_H='hpnicfObjectInfoTypeExtension'
_G='hpnicfObjectInfoType'
_F='hpnicfObjectInfoOID'
_E='Integer32'
_D='OctetString'
_C='not-accessible'
_B='HPN-ICF-OBJECT-INFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfObjectInfo=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,55))
if mibBuilder.loadTexts:hpnicfObjectInfo.setRevisions(('2004-12-27 00:00',))
_HpnicfObjectInformation_ObjectIdentity=ObjectIdentity
hpnicfObjectInformation=_HpnicfObjectInformation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,55,1))
_HpnicfObjectInfoTable_Object=MibTable
hpnicfObjectInfoTable=_HpnicfObjectInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1))
if mibBuilder.loadTexts:hpnicfObjectInfoTable.setStatus(_A)
_HpnicfObjectInfoEntry_Object=MibTableRow
hpnicfObjectInfoEntry=_HpnicfObjectInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1,1))
hpnicfObjectInfoEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfObjectInfoEntry.setStatus(_A)
_HpnicfObjectInfoOID_Type=ObjectIdentifier
_HpnicfObjectInfoOID_Object=MibTableColumn
hpnicfObjectInfoOID=_HpnicfObjectInfoOID_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1,1,1),_HpnicfObjectInfoOID_Type())
hpnicfObjectInfoOID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjectInfoOID.setStatus(_A)
class _HpnicfObjectInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('reserved',1),('accessType',2),('dataType',3),('dataRange',4),('dataLength',5)))
_HpnicfObjectInfoType_Type.__name__=_E
_HpnicfObjectInfoType_Object=MibTableColumn
hpnicfObjectInfoType=_HpnicfObjectInfoType_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1,1,2),_HpnicfObjectInfoType_Type())
hpnicfObjectInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjectInfoType.setStatus(_A)
class _HpnicfObjectInfoTypeExtension_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfObjectInfoTypeExtension_Type.__name__=_D
_HpnicfObjectInfoTypeExtension_Object=MibTableColumn
hpnicfObjectInfoTypeExtension=_HpnicfObjectInfoTypeExtension_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1,1,3),_HpnicfObjectInfoTypeExtension_Type())
hpnicfObjectInfoTypeExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjectInfoTypeExtension.setStatus(_A)
_HpnicfObjectInfoValue_Type=OctetString
_HpnicfObjectInfoValue_Object=MibTableColumn
hpnicfObjectInfoValue=_HpnicfObjectInfoValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,55,1,1,1,4),_HpnicfObjectInfoValue_Type())
hpnicfObjectInfoValue.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfObjectInfoValue.setStatus(_A)
_HpnicfObjectInfoMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfObjectInfoMIBConformance=_HpnicfObjectInfoMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,55,2))
_HpnicfObjectInfoMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfObjectInfoMIBCompliances=_HpnicfObjectInfoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,55,2,1))
_HpnicfObjectInfoMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfObjectInfoMIBGroups=_HpnicfObjectInfoMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,55,2,2))
hpnicfObjectInfoTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,55,2,2,1))
hpnicfObjectInfoTableGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:hpnicfObjectInfoTableGroup.setStatus(_A)
hpnicfObjectInfoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,55,2,1,1))
hpnicfObjectInfoMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:hpnicfObjectInfoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfObjectInfo':hpnicfObjectInfo,'hpnicfObjectInformation':hpnicfObjectInformation,'hpnicfObjectInfoTable':hpnicfObjectInfoTable,'hpnicfObjectInfoEntry':hpnicfObjectInfoEntry,_F:hpnicfObjectInfoOID,_G:hpnicfObjectInfoType,_H:hpnicfObjectInfoTypeExtension,_I:hpnicfObjectInfoValue,'hpnicfObjectInfoMIBConformance':hpnicfObjectInfoMIBConformance,'hpnicfObjectInfoMIBCompliances':hpnicfObjectInfoMIBCompliances,'hpnicfObjectInfoMIBCompliance':hpnicfObjectInfoMIBCompliance,'hpnicfObjectInfoMIBGroups':hpnicfObjectInfoMIBGroups,_J:hpnicfObjectInfoTableGroup})