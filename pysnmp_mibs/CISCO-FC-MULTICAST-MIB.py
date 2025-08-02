_L='cfmConfigurationGroup'
_K='cfmMulticastRootRowStatus'
_J='cfmMulticastRootDomainId'
_I='cfmMulticastRootOperMode'
_H='cfmMulticastRootConfigMode'
_G='read-only'
_F='read-create'
_E='CfmMulticastRootMode'
_D='vsanIndex'
_C='CISCO-VSAN-MIB'
_B='CISCO-FC-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DomainIdOrZero,=mibBuilder.importSymbols('CISCO-ST-TC','DomainIdOrZero')
vsanIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoFcMulticastMIB=ModuleIdentity((1,3,6,1,4,1,9,9,435))
if mibBuilder.loadTexts:ciscoFcMulticastMIB.setRevisions(('2004-10-07 00:00',))
class CfmMulticastRootMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('principalSwitch',1),('lowestDomainSwitch',2)))
_CiscoFcMulticastNotifications_ObjectIdentity=ObjectIdentity
ciscoFcMulticastNotifications=_CiscoFcMulticastNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,435,0))
_CiscoFcMulticastMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcMulticastMIBObjects=_CiscoFcMulticastMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,435,1))
_CfmConfiguration_ObjectIdentity=ObjectIdentity
cfmConfiguration=_CfmConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,435,1,1))
_CfmMulticastRootTable_Object=MibTable
cfmMulticastRootTable=_CfmMulticastRootTable_Object((1,3,6,1,4,1,9,9,435,1,1,1))
if mibBuilder.loadTexts:cfmMulticastRootTable.setStatus(_A)
_CfmMulticastRootEntry_Object=MibTableRow
cfmMulticastRootEntry=_CfmMulticastRootEntry_Object((1,3,6,1,4,1,9,9,435,1,1,1,1))
cfmMulticastRootEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cfmMulticastRootEntry.setStatus(_A)
class _CfmMulticastRootConfigMode_Type(CfmMulticastRootMode):defaultValue=1
_CfmMulticastRootConfigMode_Type.__name__=_E
_CfmMulticastRootConfigMode_Object=MibTableColumn
cfmMulticastRootConfigMode=_CfmMulticastRootConfigMode_Object((1,3,6,1,4,1,9,9,435,1,1,1,1,1),_CfmMulticastRootConfigMode_Type())
cfmMulticastRootConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmMulticastRootConfigMode.setStatus(_A)
_CfmMulticastRootOperMode_Type=CfmMulticastRootMode
_CfmMulticastRootOperMode_Object=MibTableColumn
cfmMulticastRootOperMode=_CfmMulticastRootOperMode_Object((1,3,6,1,4,1,9,9,435,1,1,1,1,2),_CfmMulticastRootOperMode_Type())
cfmMulticastRootOperMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmMulticastRootOperMode.setStatus(_A)
_CfmMulticastRootDomainId_Type=DomainIdOrZero
_CfmMulticastRootDomainId_Object=MibTableColumn
cfmMulticastRootDomainId=_CfmMulticastRootDomainId_Object((1,3,6,1,4,1,9,9,435,1,1,1,1,3),_CfmMulticastRootDomainId_Type())
cfmMulticastRootDomainId.setMaxAccess(_G)
if mibBuilder.loadTexts:cfmMulticastRootDomainId.setStatus(_A)
_CfmMulticastRootRowStatus_Type=RowStatus
_CfmMulticastRootRowStatus_Object=MibTableColumn
cfmMulticastRootRowStatus=_CfmMulticastRootRowStatus_Object((1,3,6,1,4,1,9,9,435,1,1,1,1,4),_CfmMulticastRootRowStatus_Type())
cfmMulticastRootRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cfmMulticastRootRowStatus.setStatus(_A)
_CiscoFcMulticaseConformance_ObjectIdentity=ObjectIdentity
ciscoFcMulticaseConformance=_CiscoFcMulticaseConformance_ObjectIdentity((1,3,6,1,4,1,9,9,435,2))
_CiscoFcMulticastMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFcMulticastMIBCompliances=_CiscoFcMulticastMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,435,2,1))
_CiscoFcMulticastMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFcMulticastMIBGroups=_CiscoFcMulticastMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,435,2,2))
cfmConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,435,2,2,1))
cfmConfigurationGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cfmConfigurationGroup.setStatus(_A)
ciscoFcMulticastMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,435,2,1,1))
ciscoFcMulticastMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoFcMulticastMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_E:CfmMulticastRootMode,'ciscoFcMulticastMIB':ciscoFcMulticastMIB,'ciscoFcMulticastNotifications':ciscoFcMulticastNotifications,'ciscoFcMulticastMIBObjects':ciscoFcMulticastMIBObjects,'cfmConfiguration':cfmConfiguration,'cfmMulticastRootTable':cfmMulticastRootTable,'cfmMulticastRootEntry':cfmMulticastRootEntry,_H:cfmMulticastRootConfigMode,_I:cfmMulticastRootOperMode,_J:cfmMulticastRootDomainId,_K:cfmMulticastRootRowStatus,'ciscoFcMulticaseConformance':ciscoFcMulticaseConformance,'ciscoFcMulticastMIBCompliances':ciscoFcMulticastMIBCompliances,'ciscoFcMulticastMIBCompliance':ciscoFcMulticastMIBCompliance,'ciscoFcMulticastMIBGroups':ciscoFcMulticastMIBGroups,_L:cfmConfigurationGroup})