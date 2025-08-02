_L='cfmaApplGroup'
_K='cfmaApplPoolId'
_J='cfmaApplHighWaterInuseFGIDs'
_I='cfmaApplInuseFgids'
_H='cfmaApplName'
_G='cfmaApplId'
_F='SnmpAdminString'
_E='entLogicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-FABRIC-MCAST-APPL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfmPoolIndex,=mibBuilder.importSymbols('CISCO-FABRIC-MCAST-MIB','CfmPoolIndex')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entLogicalIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoFabricMcastApplMIB=ModuleIdentity((1,3,6,1,4,1,9,9,256))
if mibBuilder.loadTexts:ciscoFabricMcastApplMIB.setRevisions(('2002-12-18 00:00',))
_CiscoFabricMcastApplMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFabricMcastApplMIBObjects=_CiscoFabricMcastApplMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,256,1))
_CfmaAppl_ObjectIdentity=ObjectIdentity
cfmaAppl=_CfmaAppl_ObjectIdentity((1,3,6,1,4,1,9,9,256,1,1))
_CfmaApplTable_Object=MibTable
cfmaApplTable=_CfmaApplTable_Object((1,3,6,1,4,1,9,9,256,1,1,1))
if mibBuilder.loadTexts:cfmaApplTable.setStatus(_A)
_CfmaApplEntry_Object=MibTableRow
cfmaApplEntry=_CfmaApplEntry_Object((1,3,6,1,4,1,9,9,256,1,1,1,1))
cfmaApplEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:cfmaApplEntry.setStatus(_A)
_CfmaApplId_Type=Unsigned32
_CfmaApplId_Object=MibTableColumn
cfmaApplId=_CfmaApplId_Object((1,3,6,1,4,1,9,9,256,1,1,1,1,1),_CfmaApplId_Type())
cfmaApplId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfmaApplId.setStatus(_A)
class _CfmaApplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CfmaApplName_Type.__name__=_F
_CfmaApplName_Object=MibTableColumn
cfmaApplName=_CfmaApplName_Object((1,3,6,1,4,1,9,9,256,1,1,1,1,2),_CfmaApplName_Type())
cfmaApplName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmaApplName.setStatus(_A)
_CfmaApplInuseFgids_Type=Gauge32
_CfmaApplInuseFgids_Object=MibTableColumn
cfmaApplInuseFgids=_CfmaApplInuseFgids_Object((1,3,6,1,4,1,9,9,256,1,1,1,1,3),_CfmaApplInuseFgids_Type())
cfmaApplInuseFgids.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmaApplInuseFgids.setStatus(_A)
if mibBuilder.loadTexts:cfmaApplInuseFgids.setUnits('fgid')
_CfmaApplHighWaterInuseFGIDs_Type=Gauge32
_CfmaApplHighWaterInuseFGIDs_Object=MibTableColumn
cfmaApplHighWaterInuseFGIDs=_CfmaApplHighWaterInuseFGIDs_Object((1,3,6,1,4,1,9,9,256,1,1,1,1,4),_CfmaApplHighWaterInuseFGIDs_Type())
cfmaApplHighWaterInuseFGIDs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmaApplHighWaterInuseFGIDs.setStatus(_A)
if mibBuilder.loadTexts:cfmaApplHighWaterInuseFGIDs.setUnits('fgid')
_CfmaApplPoolId_Type=CfmPoolIndex
_CfmaApplPoolId_Object=MibTableColumn
cfmaApplPoolId=_CfmaApplPoolId_Object((1,3,6,1,4,1,9,9,256,1,1,1,1,5),_CfmaApplPoolId_Type())
cfmaApplPoolId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmaApplPoolId.setStatus(_A)
_CfmaMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cfmaMIBNotificationPrefix=_CfmaMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,256,2))
_CfmaMIBNotifications_ObjectIdentity=ObjectIdentity
cfmaMIBNotifications=_CfmaMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,256,2,0))
_CfmaMIBConformance_ObjectIdentity=ObjectIdentity
cfmaMIBConformance=_CfmaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,256,3))
_CfmaMIBCompliances_ObjectIdentity=ObjectIdentity
cfmaMIBCompliances=_CfmaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,256,3,1))
_CfmaMIBGroups_ObjectIdentity=ObjectIdentity
cfmaMIBGroups=_CfmaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,256,3,2))
cfmaApplGroup=ObjectGroup((1,3,6,1,4,1,9,9,256,3,2,1))
cfmaApplGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cfmaApplGroup.setStatus(_A)
cfmaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,256,3,1,1))
cfmaMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:cfmaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFabricMcastApplMIB':ciscoFabricMcastApplMIB,'ciscoFabricMcastApplMIBObjects':ciscoFabricMcastApplMIBObjects,'cfmaAppl':cfmaAppl,'cfmaApplTable':cfmaApplTable,'cfmaApplEntry':cfmaApplEntry,_G:cfmaApplId,_H:cfmaApplName,_I:cfmaApplInuseFgids,_J:cfmaApplHighWaterInuseFGIDs,_K:cfmaApplPoolId,'cfmaMIBNotificationPrefix':cfmaMIBNotificationPrefix,'cfmaMIBNotifications':cfmaMIBNotifications,'cfmaMIBConformance':cfmaMIBConformance,'cfmaMIBCompliances':cfmaMIBCompliances,'cfmaMIBCompliance':cfmaMIBCompliance,'cfmaMIBGroups':cfmaMIBGroups,_L:cfmaApplGroup})