_Y='ciscoDnacAlarmGroup'
_X='ciscoDnacObjectGroup'
_W='cDnacAlarm'
_V='cDnacIndex'
_U='Integer32'
_T='SnmpAdminString'
_S='OctetString'
_R='cDnacUserMessage'
_Q='cDnacSource'
_P='cDnacSeverity'
_O='cDnacType'
_N='cDnacCategory'
_M='cDnacSubDomain'
_L='cDnacDomain'
_K='cDnacTimestamp'
_J='cDnacVersion'
_I='cDnacTags'
_H='cDnacDescription'
_G='cDnacName'
_F='cDnacEventID'
_E='cDnacInstanceID'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-DNAC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_U,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoDnacMIB=ModuleIdentity((1,3,6,1,4,1,9,9,867))
if mibBuilder.loadTexts:ciscoDnacMIB.setRevisions(('2019-08-15 00:00','2019-08-13 00:00'))
_CiscoDnacMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDnacMIBNotifs=_CiscoDnacMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,867,0))
_CiscoDnacMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDnacMIBObjects=_CiscoDnacMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,867,1))
_CDnacAlarms_ObjectIdentity=ObjectIdentity
cDnacAlarms=_CDnacAlarms_ObjectIdentity((1,3,6,1,4,1,9,9,867,1,1))
class _CDnacAlarmsMax_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CDnacAlarmsMax_Type.__name__=_D
_CDnacAlarmsMax_Object=MibScalar
cDnacAlarmsMax=_CDnacAlarmsMax_Object((1,3,6,1,4,1,9,9,867,1,1,1),_CDnacAlarmsMax_Type())
cDnacAlarmsMax.setMaxAccess('read-write')
if mibBuilder.loadTexts:cDnacAlarmsMax.setStatus(_B)
_CDnacAlarmsTable_Object=MibTable
cDnacAlarmsTable=_CDnacAlarmsTable_Object((1,3,6,1,4,1,9,9,867,1,1,2))
if mibBuilder.loadTexts:cDnacAlarmsTable.setStatus(_B)
_CDnacAlarmEntry_Object=MibTableRow
cDnacAlarmEntry=_CDnacAlarmEntry_Object((1,3,6,1,4,1,9,9,867,1,1,2,1))
cDnacAlarmEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:cDnacAlarmEntry.setStatus(_B)
class _CDnacIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CDnacIndex_Type.__name__=_D
_CDnacIndex_Object=MibTableColumn
cDnacIndex=_CDnacIndex_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,1),_CDnacIndex_Type())
cDnacIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cDnacIndex.setStatus(_B)
_CDnacInstanceID_Type=SnmpAdminString
_CDnacInstanceID_Object=MibTableColumn
cDnacInstanceID=_CDnacInstanceID_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,2),_CDnacInstanceID_Type())
cDnacInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacInstanceID.setStatus(_B)
_CDnacEventID_Type=SnmpAdminString
_CDnacEventID_Object=MibTableColumn
cDnacEventID=_CDnacEventID_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,3),_CDnacEventID_Type())
cDnacEventID.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacEventID.setStatus(_B)
_CDnacName_Type=SnmpAdminString
_CDnacName_Object=MibTableColumn
cDnacName=_CDnacName_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,4),_CDnacName_Type())
cDnacName.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacName.setStatus(_B)
_CDnacDescription_Type=SnmpAdminString
_CDnacDescription_Object=MibTableColumn
cDnacDescription=_CDnacDescription_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,5),_CDnacDescription_Type())
cDnacDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacDescription.setStatus(_B)
_CDnacTags_Type=SnmpAdminString
_CDnacTags_Object=MibTableColumn
cDnacTags=_CDnacTags_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,6),_CDnacTags_Type())
cDnacTags.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacTags.setStatus(_B)
_CDnacVersion_Type=SnmpAdminString
_CDnacVersion_Object=MibTableColumn
cDnacVersion=_CDnacVersion_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,7),_CDnacVersion_Type())
cDnacVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacVersion.setStatus(_B)
_CDnacTimestamp_Type=TimeStamp
_CDnacTimestamp_Object=MibTableColumn
cDnacTimestamp=_CDnacTimestamp_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,8),_CDnacTimestamp_Type())
cDnacTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacTimestamp.setStatus(_B)
_CDnacDomain_Type=SnmpAdminString
_CDnacDomain_Object=MibTableColumn
cDnacDomain=_CDnacDomain_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,9),_CDnacDomain_Type())
cDnacDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacDomain.setStatus(_B)
_CDnacSubDomain_Type=SnmpAdminString
_CDnacSubDomain_Object=MibTableColumn
cDnacSubDomain=_CDnacSubDomain_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,10),_CDnacSubDomain_Type())
cDnacSubDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacSubDomain.setStatus(_B)
_CDnacCategory_Type=SnmpAdminString
_CDnacCategory_Object=MibTableColumn
cDnacCategory=_CDnacCategory_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,11),_CDnacCategory_Type())
cDnacCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacCategory.setStatus(_B)
class _CDnacType_Type(SnmpAdminString):defaultValue=OctetString('SYSTEM')
_CDnacType_Type.__name__=_T
_CDnacType_Object=MibTableColumn
cDnacType=_CDnacType_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,12),_CDnacType_Type())
cDnacType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacType.setStatus(_B)
class _CDnacSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_CDnacSeverity_Type.__name__=_U
_CDnacSeverity_Object=MibTableColumn
cDnacSeverity=_CDnacSeverity_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,13),_CDnacSeverity_Type())
cDnacSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacSeverity.setStatus(_B)
_CDnacSource_Type=SnmpAdminString
_CDnacSource_Object=MibTableColumn
cDnacSource=_CDnacSource_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,14),_CDnacSource_Type())
cDnacSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacSource.setStatus(_B)
class _CDnacUserMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_CDnacUserMessage_Type.__name__=_S
_CDnacUserMessage_Object=MibTableColumn
cDnacUserMessage=_CDnacUserMessage_Object((1,3,6,1,4,1,9,9,867,1,1,2,1,15),_CDnacUserMessage_Type())
cDnacUserMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cDnacUserMessage.setStatus(_B)
_CiscoDnacMIBConform_ObjectIdentity=ObjectIdentity
ciscoDnacMIBConform=_CiscoDnacMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,867,2))
_CiscoDnacMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDnacMIBCompliances=_CiscoDnacMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,867,2,1))
_CiscoDnacMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDnacMIBGroups=_CiscoDnacMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,867,2,2))
ciscoDnacObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,867,2,2,1))
ciscoDnacObjectGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoDnacObjectGroup.setStatus(_B)
cDnacAlarm=NotificationType((1,3,6,1,4,1,9,9,867,0,1))
cDnacAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cDnacAlarm.setStatus(_B)
ciscoDnacAlarmGroup=NotificationGroup((1,3,6,1,4,1,9,9,867,2,2,2))
ciscoDnacAlarmGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoDnacAlarmGroup.setStatus(_B)
ciscoDnacMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,867,2,1,1))
ciscoDnacMIBCompliance.setObjects(*((_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoDnacMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDnacMIB':ciscoDnacMIB,'ciscoDnacMIBNotifs':ciscoDnacMIBNotifs,_W:cDnacAlarm,'ciscoDnacMIBObjects':ciscoDnacMIBObjects,'cDnacAlarms':cDnacAlarms,'cDnacAlarmsMax':cDnacAlarmsMax,'cDnacAlarmsTable':cDnacAlarmsTable,'cDnacAlarmEntry':cDnacAlarmEntry,_V:cDnacIndex,_E:cDnacInstanceID,_F:cDnacEventID,_G:cDnacName,_H:cDnacDescription,_I:cDnacTags,_J:cDnacVersion,_K:cDnacTimestamp,_L:cDnacDomain,_M:cDnacSubDomain,_N:cDnacCategory,_O:cDnacType,_P:cDnacSeverity,_Q:cDnacSource,_R:cDnacUserMessage,'ciscoDnacMIBConform':ciscoDnacMIBConform,'ciscoDnacMIBCompliances':ciscoDnacMIBCompliances,'ciscoDnacMIBCompliance':ciscoDnacMIBCompliance,'ciscoDnacMIBGroups':ciscoDnacMIBGroups,_X:ciscoDnacObjectGroup,_Y:ciscoDnacAlarmGroup})