_L='ciscoSnmpVacmExtGroup'
_K='cvacmSecurityGrpStatus'
_J='cvacmSecurityGrpStorageType'
_I='read-create'
_H='cvacmSecurityGrpName'
_G='StorageType'
_F='vacmSecurityName'
_E='vacmSecurityModel'
_D='SnmpAdminString'
_C='SNMP-VIEW-BASED-ACM-MIB'
_B='CISCO-SNMP-VACM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
vacmSecurityModel,vacmSecurityName=mibBuilder.importSymbols(_C,_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention')
ciscoSnmpVacmExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,409))
if mibBuilder.loadTexts:ciscoSnmpVacmExtMIB.setRevisions(('2004-05-19 00:00',))
_CiscoSnmpVacmExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSnmpVacmExtMIBObjects=_CiscoSnmpVacmExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,409,1))
_CvacmSecurityToGroupTable_Object=MibTable
cvacmSecurityToGroupTable=_CvacmSecurityToGroupTable_Object((1,3,6,1,4,1,9,9,409,1,1))
if mibBuilder.loadTexts:cvacmSecurityToGroupTable.setStatus(_A)
_CvacmSecurityToGroupEntry_Object=MibTableRow
cvacmSecurityToGroupEntry=_CvacmSecurityToGroupEntry_Object((1,3,6,1,4,1,9,9,409,1,1,1))
cvacmSecurityToGroupEntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_B,_H))
if mibBuilder.loadTexts:cvacmSecurityToGroupEntry.setStatus(_A)
class _CvacmSecurityGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvacmSecurityGrpName_Type.__name__=_D
_CvacmSecurityGrpName_Object=MibTableColumn
cvacmSecurityGrpName=_CvacmSecurityGrpName_Object((1,3,6,1,4,1,9,9,409,1,1,1,1),_CvacmSecurityGrpName_Type())
cvacmSecurityGrpName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvacmSecurityGrpName.setStatus(_A)
class _CvacmSecurityGrpStorageType_Type(StorageType):defaultValue=3
_CvacmSecurityGrpStorageType_Type.__name__=_G
_CvacmSecurityGrpStorageType_Object=MibTableColumn
cvacmSecurityGrpStorageType=_CvacmSecurityGrpStorageType_Object((1,3,6,1,4,1,9,9,409,1,1,1,2),_CvacmSecurityGrpStorageType_Type())
cvacmSecurityGrpStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:cvacmSecurityGrpStorageType.setStatus(_A)
_CvacmSecurityGrpStatus_Type=RowStatus
_CvacmSecurityGrpStatus_Object=MibTableColumn
cvacmSecurityGrpStatus=_CvacmSecurityGrpStatus_Object((1,3,6,1,4,1,9,9,409,1,1,1,3),_CvacmSecurityGrpStatus_Type())
cvacmSecurityGrpStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cvacmSecurityGrpStatus.setStatus(_A)
_CiscoSnmpVacmExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSnmpVacmExtMIBConformance=_CiscoSnmpVacmExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,409,2))
_CiscoSnmpVacmExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSnmpVacmExtMIBCompliances=_CiscoSnmpVacmExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,409,2,1))
_CiscoSnmpVacmExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSnmpVacmExtMIBGroups=_CiscoSnmpVacmExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,409,2,2))
ciscoSnmpVacmExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,409,2,2,1))
ciscoSnmpVacmExtGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoSnmpVacmExtGroup.setStatus(_A)
ciscoSnmpVacmExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,409,2,1,1))
ciscoSnmpVacmExtMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoSnmpVacmExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSnmpVacmExtMIB':ciscoSnmpVacmExtMIB,'ciscoSnmpVacmExtMIBObjects':ciscoSnmpVacmExtMIBObjects,'cvacmSecurityToGroupTable':cvacmSecurityToGroupTable,'cvacmSecurityToGroupEntry':cvacmSecurityToGroupEntry,_H:cvacmSecurityGrpName,_J:cvacmSecurityGrpStorageType,_K:cvacmSecurityGrpStatus,'ciscoSnmpVacmExtMIBConformance':ciscoSnmpVacmExtMIBConformance,'ciscoSnmpVacmExtMIBCompliances':ciscoSnmpVacmExtMIBCompliances,'ciscoSnmpVacmExtMIBCompliance':ciscoSnmpVacmExtMIBCompliance,'ciscoSnmpVacmExtMIBGroups':ciscoSnmpVacmExtMIBGroups,_L:ciscoSnmpVacmExtGroup})