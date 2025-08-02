_M='pdnPortConfigVnidId'
_L='pdnClientConfigVnidId'
_K='pdnClientConfigAddr'
_J='pdnCardConfigVnidId'
_I='NotificationType'
_H='pdnClientConfigSubnetMask'
_G='Integer32'
_F='PDN-DOMAIN-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
pdn_domain,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-domain')
ClientState,SwitchState,VnidRange,VnidTaggingState=mibBuilder.importSymbols('PDN-TC','ClientState','SwitchState','VnidRange','VnidTaggingState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
_PdnDomainMIBObjects_ObjectIdentity=ObjectIdentity
pdnDomainMIBObjects=_PdnDomainMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,1))
_PdnCardGeneralParams_ObjectIdentity=ObjectIdentity
pdnCardGeneralParams=_PdnCardGeneralParams_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,1,1))
_PdnCardGeneralParamsVNIDMode_Type=VnidTaggingState
_PdnCardGeneralParamsVNIDMode_Object=MibScalar
pdnCardGeneralParamsVNIDMode=_PdnCardGeneralParamsVNIDMode_Object((1,3,6,1,4,1,1795,2,24,2,22,1,1,1),_PdnCardGeneralParamsVNIDMode_Type())
pdnCardGeneralParamsVNIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardGeneralParamsVNIDMode.setStatus(_A)
_PdnCardConfig_ObjectIdentity=ObjectIdentity
pdnCardConfig=_PdnCardConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,1,2))
_PdnCardConfigTable_Object=MibTable
pdnCardConfigTable=_PdnCardConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1))
if mibBuilder.loadTexts:pdnCardConfigTable.setStatus(_A)
_PdnCardConfigEntry_Object=MibTableRow
pdnCardConfigEntry=_PdnCardConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1))
pdnCardConfigEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:pdnCardConfigEntry.setStatus(_A)
_PdnCardConfigVnidId_Type=VnidRange
_PdnCardConfigVnidId_Object=MibTableColumn
pdnCardConfigVnidId=_PdnCardConfigVnidId_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,1),_PdnCardConfigVnidId_Type())
pdnCardConfigVnidId.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCardConfigVnidId.setStatus(_A)
_PdnCardConfigDomainName_Type=DisplayString
_PdnCardConfigDomainName_Object=MibTableColumn
pdnCardConfigDomainName=_PdnCardConfigDomainName_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,2),_PdnCardConfigDomainName_Type())
pdnCardConfigDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigDomainName.setStatus(_A)
_PdnCardConfigMuxFwd_Type=SwitchState
_PdnCardConfigMuxFwd_Object=MibTableColumn
pdnCardConfigMuxFwd=_PdnCardConfigMuxFwd_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,3),_PdnCardConfigMuxFwd_Type())
pdnCardConfigMuxFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigMuxFwd.setStatus(_A)
_PdnCardConfigIPFiltering_Type=SwitchState
_PdnCardConfigIPFiltering_Object=MibTableColumn
pdnCardConfigIPFiltering=_PdnCardConfigIPFiltering_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,4),_PdnCardConfigIPFiltering_Type())
pdnCardConfigIPFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigIPFiltering.setStatus(_A)
_PdnCardConfigIPScoping_Type=SwitchState
_PdnCardConfigIPScoping_Object=MibTableColumn
pdnCardConfigIPScoping=_PdnCardConfigIPScoping_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,5),_PdnCardConfigIPScoping_Type())
pdnCardConfigIPScoping.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigIPScoping.setStatus(_A)
_PdnCardConfigVnidAuth_Type=SwitchState
_PdnCardConfigVnidAuth_Object=MibTableColumn
pdnCardConfigVnidAuth=_PdnCardConfigVnidAuth_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,6),_PdnCardConfigVnidAuth_Type())
pdnCardConfigVnidAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigVnidAuth.setStatus(_A)
_PdnCardConfigRowStatus_Type=RowStatus
_PdnCardConfigRowStatus_Object=MibTableColumn
pdnCardConfigRowStatus=_PdnCardConfigRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,22,1,2,1,1,7),_PdnCardConfigRowStatus_Type())
pdnCardConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnCardConfigRowStatus.setStatus(_A)
_PdnClientConfig_ObjectIdentity=ObjectIdentity
pdnClientConfig=_PdnClientConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,1,3))
_PdnClientConfigTable_Object=MibTable
pdnClientConfigTable=_PdnClientConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1))
if mibBuilder.loadTexts:pdnClientConfigTable.setStatus(_A)
_PdnClientConfigEntry_Object=MibTableRow
pdnClientConfigEntry=_PdnClientConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1))
pdnClientConfigEntry.setIndexNames((0,_D,_E),(0,_F,_K),(0,_F,_H),(0,_F,_L))
if mibBuilder.loadTexts:pdnClientConfigEntry.setStatus(_A)
_PdnClientConfigAddr_Type=IpAddress
_PdnClientConfigAddr_Object=MibTableColumn
pdnClientConfigAddr=_PdnClientConfigAddr_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,1),_PdnClientConfigAddr_Type())
pdnClientConfigAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigAddr.setStatus(_A)
_PdnClientConfigSubnetMask_Type=IpAddress
_PdnClientConfigSubnetMask_Object=MibTableColumn
pdnClientConfigSubnetMask=_PdnClientConfigSubnetMask_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,2),_PdnClientConfigSubnetMask_Type())
pdnClientConfigSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigSubnetMask.setStatus(_A)
_PdnClientConfigVnidId_Type=VnidRange
_PdnClientConfigVnidId_Object=MibTableColumn
pdnClientConfigVnidId=_PdnClientConfigVnidId_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,3),_PdnClientConfigVnidId_Type())
pdnClientConfigVnidId.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigVnidId.setStatus(_A)
_PdnClientConfigNHR_Type=IpAddress
_PdnClientConfigNHR_Object=MibTableColumn
pdnClientConfigNHR=_PdnClientConfigNHR_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,4),_PdnClientConfigNHR_Type())
pdnClientConfigNHR.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnClientConfigNHR.setStatus(_A)
_PdnClientConfigType_Type=ClientState
_PdnClientConfigType_Object=MibTableColumn
pdnClientConfigType=_PdnClientConfigType_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,5),_PdnClientConfigType_Type())
pdnClientConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigType.setStatus(_A)
_PdnClientConfigLeaseTime_Type=TimeTicks
_PdnClientConfigLeaseTime_Object=MibTableColumn
pdnClientConfigLeaseTime=_PdnClientConfigLeaseTime_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,6),_PdnClientConfigLeaseTime_Type())
pdnClientConfigLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigLeaseTime.setStatus(_A)
_PdnClientConfigLeaseRemainTime_Type=TimeTicks
_PdnClientConfigLeaseRemainTime_Object=MibTableColumn
pdnClientConfigLeaseRemainTime=_PdnClientConfigLeaseRemainTime_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,7),_PdnClientConfigLeaseRemainTime_Type())
pdnClientConfigLeaseRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigLeaseRemainTime.setStatus(_A)
_PdnClientConfigMacAddr_Type=MacAddress
_PdnClientConfigMacAddr_Object=MibTableColumn
pdnClientConfigMacAddr=_PdnClientConfigMacAddr_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,8),_PdnClientConfigMacAddr_Type())
pdnClientConfigMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientConfigMacAddr.setStatus(_A)
_PdnClientConfigRowStatus_Type=RowStatus
_PdnClientConfigRowStatus_Object=MibTableColumn
pdnClientConfigRowStatus=_PdnClientConfigRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,1,1,9),_PdnClientConfigRowStatus_Type())
pdnClientConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnClientConfigRowStatus.setStatus(_A)
_PdnMaxClientsTable_Object=MibTable
pdnMaxClientsTable=_PdnMaxClientsTable_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,2))
if mibBuilder.loadTexts:pdnMaxClientsTable.setStatus(_A)
_PdnMaxClientsEntry_Object=MibTableRow
pdnMaxClientsEntry=_PdnMaxClientsEntry_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,2,1))
pdnMaxClientsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pdnMaxClientsEntry.setStatus(_A)
class _PdnMaxClients_Type(Integer32):defaultValue=32
_PdnMaxClients_Type.__name__=_G
_PdnMaxClients_Object=MibTableColumn
pdnMaxClients=_PdnMaxClients_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,2,1,1),_PdnMaxClients_Type())
pdnMaxClients.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnMaxClients.setStatus(_A)
class _PdnMaxDynamicClients_Type(Integer32):defaultValue=0
_PdnMaxDynamicClients_Type.__name__=_G
_PdnMaxDynamicClients_Object=MibTableColumn
pdnMaxDynamicClients=_PdnMaxDynamicClients_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,2,1,2),_PdnMaxDynamicClients_Type())
pdnMaxDynamicClients.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnMaxDynamicClients.setStatus(_A)
_PdnClientAdditionalClientsAvailable_Type=Integer32
_PdnClientAdditionalClientsAvailable_Object=MibScalar
pdnClientAdditionalClientsAvailable=_PdnClientAdditionalClientsAvailable_Object((1,3,6,1,4,1,1795,2,24,2,22,1,3,3),_PdnClientAdditionalClientsAvailable_Type())
pdnClientAdditionalClientsAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnClientAdditionalClientsAvailable.setStatus(_A)
_PdnPortConfig_ObjectIdentity=ObjectIdentity
pdnPortConfig=_PdnPortConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,1,4))
_PdnPortConfigTable_Object=MibTable
pdnPortConfigTable=_PdnPortConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1))
if mibBuilder.loadTexts:pdnPortConfigTable.setStatus(_A)
_PdnPortConfigEntry_Object=MibTableRow
pdnPortConfigEntry=_PdnPortConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1,1))
pdnPortConfigEntry.setIndexNames((0,_D,_E),(0,_F,_M))
if mibBuilder.loadTexts:pdnPortConfigEntry.setStatus(_A)
_PdnPortConfigVnidId_Type=VnidRange
_PdnPortConfigVnidId_Object=MibTableColumn
pdnPortConfigVnidId=_PdnPortConfigVnidId_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1,1,1),_PdnPortConfigVnidId_Type())
pdnPortConfigVnidId.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigVnidId.setStatus(_A)
class _PdnPortConfigCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('un-bind',1),('bind',2)))
_PdnPortConfigCfg_Type.__name__=_G
_PdnPortConfigCfg_Object=MibTableColumn
pdnPortConfigCfg=_PdnPortConfigCfg_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1,1,2),_PdnPortConfigCfg_Type())
pdnPortConfigCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnPortConfigCfg.setStatus(_A)
_PdnPortConfigDefNHR_Type=IpAddress
_PdnPortConfigDefNHR_Object=MibTableColumn
pdnPortConfigDefNHR=_PdnPortConfigDefNHR_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1,1,3),_PdnPortConfigDefNHR_Type())
pdnPortConfigDefNHR.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnPortConfigDefNHR.setStatus(_A)
_PdnPortConfigOperStatus_Type=SwitchState
_PdnPortConfigOperStatus_Object=MibTableColumn
pdnPortConfigOperStatus=_PdnPortConfigOperStatus_Object((1,3,6,1,4,1,1795,2,24,2,22,1,4,1,1,4),_PdnPortConfigOperStatus_Type())
pdnPortConfigOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPortConfigOperStatus.setStatus(_A)
_PdnDomainMIBTraps_ObjectIdentity=ObjectIdentity
pdnDomainMIBTraps=_PdnDomainMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,22,2))
dhcpClientHostTableFull=NotificationType((1,3,6,1,4,1,1795,2,24,2,22,2,0,1))
dhcpClientHostTableFull.setObjects((_D,_E))
if mibBuilder.loadTexts:dhcpClientHostTableFull.setStatus('')
dhcpAddressInStaticSubnet=NotificationType((1,3,6,1,4,1,1795,2,24,2,22,2,0,2))
dhcpAddressInStaticSubnet.setObjects(*((_D,_E),(_F,_H),(_D,_E)))
if mibBuilder.loadTexts:dhcpAddressInStaticSubnet.setStatus('')
mibBuilder.exportSymbols(_F,**{'pdnDomainMIBObjects':pdnDomainMIBObjects,'pdnCardGeneralParams':pdnCardGeneralParams,'pdnCardGeneralParamsVNIDMode':pdnCardGeneralParamsVNIDMode,'pdnCardConfig':pdnCardConfig,'pdnCardConfigTable':pdnCardConfigTable,'pdnCardConfigEntry':pdnCardConfigEntry,_J:pdnCardConfigVnidId,'pdnCardConfigDomainName':pdnCardConfigDomainName,'pdnCardConfigMuxFwd':pdnCardConfigMuxFwd,'pdnCardConfigIPFiltering':pdnCardConfigIPFiltering,'pdnCardConfigIPScoping':pdnCardConfigIPScoping,'pdnCardConfigVnidAuth':pdnCardConfigVnidAuth,'pdnCardConfigRowStatus':pdnCardConfigRowStatus,'pdnClientConfig':pdnClientConfig,'pdnClientConfigTable':pdnClientConfigTable,'pdnClientConfigEntry':pdnClientConfigEntry,_K:pdnClientConfigAddr,_H:pdnClientConfigSubnetMask,_L:pdnClientConfigVnidId,'pdnClientConfigNHR':pdnClientConfigNHR,'pdnClientConfigType':pdnClientConfigType,'pdnClientConfigLeaseTime':pdnClientConfigLeaseTime,'pdnClientConfigLeaseRemainTime':pdnClientConfigLeaseRemainTime,'pdnClientConfigMacAddr':pdnClientConfigMacAddr,'pdnClientConfigRowStatus':pdnClientConfigRowStatus,'pdnMaxClientsTable':pdnMaxClientsTable,'pdnMaxClientsEntry':pdnMaxClientsEntry,'pdnMaxClients':pdnMaxClients,'pdnMaxDynamicClients':pdnMaxDynamicClients,'pdnClientAdditionalClientsAvailable':pdnClientAdditionalClientsAvailable,'pdnPortConfig':pdnPortConfig,'pdnPortConfigTable':pdnPortConfigTable,'pdnPortConfigEntry':pdnPortConfigEntry,_M:pdnPortConfigVnidId,'pdnPortConfigCfg':pdnPortConfigCfg,'pdnPortConfigDefNHR':pdnPortConfigDefNHR,'pdnPortConfigOperStatus':pdnPortConfigOperStatus,'pdnDomainMIBTraps':pdnDomainMIBTraps,'dhcpClientHostTableFull':dhcpClientHostTableFull,'dhcpAddressInStaticSubnet':dhcpAddressInStaticSubnet})