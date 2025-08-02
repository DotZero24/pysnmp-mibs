_I='dpLacpExtChannelGrpInfoGroup'
_H='dpLacpExtGroupRowStatus'
_G='dpLacpExtGroupMemberPorts'
_F='dpLacpExtGroupType'
_E='dpLacpExtGroupChannelNo'
_D='read-create'
_C='Integer32'
_B='DLINKPRIME-LACP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dlinkPrimeLacpExtMIB=ModuleIdentity((1,3,6,1,4,1,171,15,6))
if mibBuilder.loadTexts:dlinkPrimeLacpExtMIB.setRevisions(('2014-04-26 00:00',))
_DpLacpExtMIBObjects_ObjectIdentity=ObjectIdentity
dpLacpExtMIBObjects=_DpLacpExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,6,1))
_DpLacpExtGroupTable_Object=MibTable
dpLacpExtGroupTable=_DpLacpExtGroupTable_Object((1,3,6,1,4,1,171,15,6,1,1))
if mibBuilder.loadTexts:dpLacpExtGroupTable.setStatus(_A)
_DpLacpExtGroupEntry_Object=MibTableRow
dpLacpExtGroupEntry=_DpLacpExtGroupEntry_Object((1,3,6,1,4,1,171,15,6,1,1,1))
dpLacpExtGroupEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dpLacpExtGroupEntry.setStatus(_A)
class _DpLacpExtGroupChannelNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DpLacpExtGroupChannelNo_Type.__name__=_C
_DpLacpExtGroupChannelNo_Object=MibTableColumn
dpLacpExtGroupChannelNo=_DpLacpExtGroupChannelNo_Object((1,3,6,1,4,1,171,15,6,1,1,1,1),_DpLacpExtGroupChannelNo_Type())
dpLacpExtGroupChannelNo.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dpLacpExtGroupChannelNo.setStatus(_A)
class _DpLacpExtGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static_on',1),('lacp_active',2),('lacp_passive',3)))
_DpLacpExtGroupType_Type.__name__=_C
_DpLacpExtGroupType_Object=MibTableColumn
dpLacpExtGroupType=_DpLacpExtGroupType_Object((1,3,6,1,4,1,171,15,6,1,1,1,2),_DpLacpExtGroupType_Type())
dpLacpExtGroupType.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLacpExtGroupType.setStatus(_A)
_DpLacpExtGroupMemberPorts_Type=PortList
_DpLacpExtGroupMemberPorts_Object=MibTableColumn
dpLacpExtGroupMemberPorts=_DpLacpExtGroupMemberPorts_Object((1,3,6,1,4,1,171,15,6,1,1,1,3),_DpLacpExtGroupMemberPorts_Type())
dpLacpExtGroupMemberPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLacpExtGroupMemberPorts.setStatus(_A)
_DpLacpExtGroupRowStatus_Type=RowStatus
_DpLacpExtGroupRowStatus_Object=MibTableColumn
dpLacpExtGroupRowStatus=_DpLacpExtGroupRowStatus_Object((1,3,6,1,4,1,171,15,6,1,1,1,4),_DpLacpExtGroupRowStatus_Type())
dpLacpExtGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpLacpExtGroupRowStatus.setStatus(_A)
_DpLacpExtMIBConformance_ObjectIdentity=ObjectIdentity
dpLacpExtMIBConformance=_DpLacpExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,6,2))
_DpLacpExtCompliances_ObjectIdentity=ObjectIdentity
dpLacpExtCompliances=_DpLacpExtCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,6,2,1))
_DpLacpExtGroups_ObjectIdentity=ObjectIdentity
dpLacpExtGroups=_DpLacpExtGroups_ObjectIdentity((1,3,6,1,4,1,171,15,6,2,2))
dpLacpExtChannelGrpInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,6,2,2,1))
dpLacpExtChannelGrpInfoGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:dpLacpExtChannelGrpInfoGroup.setStatus(_A)
dpLacpExtCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,6,2,1,1))
dpLacpExtCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:dpLacpExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeLacpExtMIB':dlinkPrimeLacpExtMIB,'dpLacpExtMIBObjects':dpLacpExtMIBObjects,'dpLacpExtGroupTable':dpLacpExtGroupTable,'dpLacpExtGroupEntry':dpLacpExtGroupEntry,_E:dpLacpExtGroupChannelNo,_F:dpLacpExtGroupType,_G:dpLacpExtGroupMemberPorts,_H:dpLacpExtGroupRowStatus,'dpLacpExtMIBConformance':dpLacpExtMIBConformance,'dpLacpExtCompliances':dpLacpExtCompliances,'dpLacpExtCompliance':dpLacpExtCompliance,'dpLacpExtGroups':dpLacpExtGroups,_I:dpLacpExtChannelGrpInfoGroup})