_K='cndeCollectorConfigurationGroup'
_J='cndeCollectorStatus'
_I='cndeMaxCollectors'
_H='cndeCollectorPort'
_G='cndeCollectorAddress'
_F='cndeCollectorAddressType'
_E='Integer32'
_D='InetAddress'
_C='not-accessible'
_B='CISCO-NDE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoNDEMIB=ModuleIdentity((1,3,6,1,4,1,9,9,226))
if mibBuilder.loadTexts:ciscoNDEMIB.setRevisions(('2006-03-01 00:00','2005-12-06 00:00','2001-08-08 00:00'))
_CndeMIBNotifs_ObjectIdentity=ObjectIdentity
cndeMIBNotifs=_CndeMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,226,0))
_CiscoNDEMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNDEMIBObjects=_CiscoNDEMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,226,1))
_CndeCollectorConfiguration_ObjectIdentity=ObjectIdentity
cndeCollectorConfiguration=_CndeCollectorConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,226,1,1))
_CndeMaxCollectors_Type=Unsigned32
_CndeMaxCollectors_Object=MibScalar
cndeMaxCollectors=_CndeMaxCollectors_Object((1,3,6,1,4,1,9,9,226,1,1,1),_CndeMaxCollectors_Type())
cndeMaxCollectors.setMaxAccess('read-only')
if mibBuilder.loadTexts:cndeMaxCollectors.setStatus(_A)
_CndeCollectorTable_Object=MibTable
cndeCollectorTable=_CndeCollectorTable_Object((1,3,6,1,4,1,9,9,226,1,1,2))
if mibBuilder.loadTexts:cndeCollectorTable.setStatus(_A)
_CndeCollectorEntry_Object=MibTableRow
cndeCollectorEntry=_CndeCollectorEntry_Object((1,3,6,1,4,1,9,9,226,1,1,2,1))
cndeCollectorEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cndeCollectorEntry.setStatus(_A)
_CndeCollectorAddressType_Type=InetAddressType
_CndeCollectorAddressType_Object=MibTableColumn
cndeCollectorAddressType=_CndeCollectorAddressType_Object((1,3,6,1,4,1,9,9,226,1,1,2,1,1),_CndeCollectorAddressType_Type())
cndeCollectorAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cndeCollectorAddressType.setStatus(_A)
class _CndeCollectorAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CndeCollectorAddress_Type.__name__=_D
_CndeCollectorAddress_Object=MibTableColumn
cndeCollectorAddress=_CndeCollectorAddress_Object((1,3,6,1,4,1,9,9,226,1,1,2,1,2),_CndeCollectorAddress_Type())
cndeCollectorAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cndeCollectorAddress.setStatus(_A)
class _CndeCollectorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CndeCollectorPort_Type.__name__=_E
_CndeCollectorPort_Object=MibTableColumn
cndeCollectorPort=_CndeCollectorPort_Object((1,3,6,1,4,1,9,9,226,1,1,2,1,3),_CndeCollectorPort_Type())
cndeCollectorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cndeCollectorPort.setStatus(_A)
_CndeCollectorStatus_Type=RowStatus
_CndeCollectorStatus_Object=MibTableColumn
cndeCollectorStatus=_CndeCollectorStatus_Object((1,3,6,1,4,1,9,9,226,1,1,2,1,4),_CndeCollectorStatus_Type())
cndeCollectorStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:cndeCollectorStatus.setStatus(_A)
_CndeMIBNotifications_ObjectIdentity=ObjectIdentity
cndeMIBNotifications=_CndeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,226,2))
_CndeMIBConformance_ObjectIdentity=ObjectIdentity
cndeMIBConformance=_CndeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,226,3))
_CndeMIBCompliances_ObjectIdentity=ObjectIdentity
cndeMIBCompliances=_CndeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,226,3,1))
_CndeMIBGroups_ObjectIdentity=ObjectIdentity
cndeMIBGroups=_CndeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,226,3,2))
cndeCollectorConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,226,3,2,1))
cndeCollectorConfigurationGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cndeCollectorConfigurationGroup.setStatus(_A)
cndeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,226,3,1,1))
cndeMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:cndeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNDEMIB':ciscoNDEMIB,'cndeMIBNotifs':cndeMIBNotifs,'ciscoNDEMIBObjects':ciscoNDEMIBObjects,'cndeCollectorConfiguration':cndeCollectorConfiguration,_I:cndeMaxCollectors,'cndeCollectorTable':cndeCollectorTable,'cndeCollectorEntry':cndeCollectorEntry,_F:cndeCollectorAddressType,_G:cndeCollectorAddress,_H:cndeCollectorPort,_J:cndeCollectorStatus,'cndeMIBNotifications':cndeMIBNotifications,'cndeMIBConformance':cndeMIBConformance,'cndeMIBCompliances':cndeMIBCompliances,'cndeMIBCompliance':cndeMIBCompliance,'cndeMIBGroups':cndeMIBGroups,_K:cndeCollectorConfigurationGroup})