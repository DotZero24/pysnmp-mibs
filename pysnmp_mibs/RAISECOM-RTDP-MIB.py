_K='raisecomRtdpRelationshipPeerDeviceId'
_J='raisecomRtdpRelationshipDeviceId'
_I='raisecomRndpDiscoveryDeviceId'
_H='RAISECOM-RNDP-MIB'
_G='RAISECOM-RTDP-MIB'
_F='mandatory'
_E='EnableVar'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomCluster,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomCluster')
raisecomRndpDiscoveryDeviceId,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC',_E,'PortList')
raisecomTopoDiscovery=ModuleIdentity((1,3,6,1,4,1,8886,1,6,2))
class _RaisecomRtdpCollectEnable_Type(EnableVar):defaultValue=2
_RaisecomRtdpCollectEnable_Type.__name__=_E
_RaisecomRtdpCollectEnable_Object=MibScalar
raisecomRtdpCollectEnable=_RaisecomRtdpCollectEnable_Object((1,3,6,1,4,1,8886,1,6,2,4),_RaisecomRtdpCollectEnable_Type())
raisecomRtdpCollectEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRtdpCollectEnable.setStatus(_F)
class _RaisecomRtdpReportEnable_Type(EnableVar):defaultValue=1
_RaisecomRtdpReportEnable_Type.__name__=_E
_RaisecomRtdpReportEnable_Object=MibScalar
raisecomRtdpReportEnable=_RaisecomRtdpReportEnable_Object((1,3,6,1,4,1,8886,1,6,2,5),_RaisecomRtdpReportEnable_Type())
raisecomRtdpReportEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRtdpReportEnable.setStatus(_F)
class _RaisecomRtdpMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_RaisecomRtdpMaxHops_Type.__name__=_C
_RaisecomRtdpMaxHops_Object=MibScalar
raisecomRtdpMaxHops=_RaisecomRtdpMaxHops_Object((1,3,6,1,4,1,8886,1,6,2,6),_RaisecomRtdpMaxHops_Type())
raisecomRtdpMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRtdpMaxHops.setStatus(_F)
_RaisecomRtdpDeviceDiscoveryTable_Object=MibTable
raisecomRtdpDeviceDiscoveryTable=_RaisecomRtdpDeviceDiscoveryTable_Object((1,3,6,1,4,1,8886,1,6,2,7))
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryTable.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryEntry_Object=MibTableRow
raisecomRtdpDeviceDiscoveryEntry=_RaisecomRtdpDeviceDiscoveryEntry_Object((1,3,6,1,4,1,8886,1,6,2,7,1))
raisecomRtdpDeviceDiscoveryEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryEntry.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryDeviceId_Type=MacAddress
_RaisecomRtdpDeviceDiscoveryDeviceId_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryDeviceId=_RaisecomRtdpDeviceDiscoveryDeviceId_Object((1,3,6,1,4,1,8886,1,6,2,7,1,1),_RaisecomRtdpDeviceDiscoveryDeviceId_Type())
raisecomRtdpDeviceDiscoveryDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryDeviceId.setStatus(_A)
class _RaisecomRtdpDeviceDiscoveryHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_RaisecomRtdpDeviceDiscoveryHops_Type.__name__=_C
_RaisecomRtdpDeviceDiscoveryHops_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryHops=_RaisecomRtdpDeviceDiscoveryHops_Object((1,3,6,1,4,1,8886,1,6,2,7,1,2),_RaisecomRtdpDeviceDiscoveryHops_Type())
raisecomRtdpDeviceDiscoveryHops.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryHops.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryHostName_Type=OctetString
_RaisecomRtdpDeviceDiscoveryHostName_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryHostName=_RaisecomRtdpDeviceDiscoveryHostName_Object((1,3,6,1,4,1,8886,1,6,2,7,1,3),_RaisecomRtdpDeviceDiscoveryHostName_Type())
raisecomRtdpDeviceDiscoveryHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryHostName.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryPlatformOid_Type=ObjectIdentifier
_RaisecomRtdpDeviceDiscoveryPlatformOid_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryPlatformOid=_RaisecomRtdpDeviceDiscoveryPlatformOid_Object((1,3,6,1,4,1,8886,1,6,2,7,1,4),_RaisecomRtdpDeviceDiscoveryPlatformOid_Type())
raisecomRtdpDeviceDiscoveryPlatformOid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryPlatformOid.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryVersion_Type=OctetString
_RaisecomRtdpDeviceDiscoveryVersion_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryVersion=_RaisecomRtdpDeviceDiscoveryVersion_Object((1,3,6,1,4,1,8886,1,6,2,7,1,5),_RaisecomRtdpDeviceDiscoveryVersion_Type())
raisecomRtdpDeviceDiscoveryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryVersion.setStatus(_A)
class _RaisecomRtdpDeviceDiscoveryCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('switch',1),('router',2),('eoa',3),('eos',4),('others',5)))
_RaisecomRtdpDeviceDiscoveryCapabilities_Type.__name__=_C
_RaisecomRtdpDeviceDiscoveryCapabilities_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryCapabilities=_RaisecomRtdpDeviceDiscoveryCapabilities_Object((1,3,6,1,4,1,8886,1,6,2,7,1,6),_RaisecomRtdpDeviceDiscoveryCapabilities_Type())
raisecomRtdpDeviceDiscoveryCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryCapabilities.setStatus(_A)
class _RaisecomRtdpDeviceDiscoveryRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('member',1),('candidate',2),('commander',3)))
_RaisecomRtdpDeviceDiscoveryRole_Type.__name__=_C
_RaisecomRtdpDeviceDiscoveryRole_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryRole=_RaisecomRtdpDeviceDiscoveryRole_Object((1,3,6,1,4,1,8886,1,6,2,7,1,7),_RaisecomRtdpDeviceDiscoveryRole_Type())
raisecomRtdpDeviceDiscoveryRole.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryRole.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryCommanderMac_Type=MacAddress
_RaisecomRtdpDeviceDiscoveryCommanderMac_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryCommanderMac=_RaisecomRtdpDeviceDiscoveryCommanderMac_Object((1,3,6,1,4,1,8886,1,6,2,7,1,8),_RaisecomRtdpDeviceDiscoveryCommanderMac_Type())
raisecomRtdpDeviceDiscoveryCommanderMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryCommanderMac.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryAutoActive_Type=EnableVar
_RaisecomRtdpDeviceDiscoveryAutoActive_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryAutoActive=_RaisecomRtdpDeviceDiscoveryAutoActive_Object((1,3,6,1,4,1,8886,1,6,2,7,1,9),_RaisecomRtdpDeviceDiscoveryAutoActive_Type())
raisecomRtdpDeviceDiscoveryAutoActive.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryAutoActive.setStatus(_A)
_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Type=MacAddress
_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Object=MibTableColumn
raisecomRtdpDeviceDiscoveryAutoActiveMac=_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Object((1,3,6,1,4,1,8886,1,6,2,7,1,10),_RaisecomRtdpDeviceDiscoveryAutoActiveMac_Type())
raisecomRtdpDeviceDiscoveryAutoActiveMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpDeviceDiscoveryAutoActiveMac.setStatus(_A)
_RaisecomRtdpRelationshipTable_Object=MibTable
raisecomRtdpRelationshipTable=_RaisecomRtdpRelationshipTable_Object((1,3,6,1,4,1,8886,1,6,2,8))
if mibBuilder.loadTexts:raisecomRtdpRelationshipTable.setStatus(_A)
_RaisecomRtdpRelationshipEntry_Object=MibTableRow
raisecomRtdpRelationshipEntry=_RaisecomRtdpRelationshipEntry_Object((1,3,6,1,4,1,8886,1,6,2,8,1))
raisecomRtdpRelationshipEntry.setIndexNames((0,_G,_J),(0,_G,_K))
if mibBuilder.loadTexts:raisecomRtdpRelationshipEntry.setStatus(_A)
_RaisecomRtdpRelationshipDeviceId_Type=MacAddress
_RaisecomRtdpRelationshipDeviceId_Object=MibTableColumn
raisecomRtdpRelationshipDeviceId=_RaisecomRtdpRelationshipDeviceId_Object((1,3,6,1,4,1,8886,1,6,2,8,1,1),_RaisecomRtdpRelationshipDeviceId_Type())
raisecomRtdpRelationshipDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpRelationshipDeviceId.setStatus(_A)
_RaisecomRtdpRelationshipPeerDeviceId_Type=MacAddress
_RaisecomRtdpRelationshipPeerDeviceId_Object=MibTableColumn
raisecomRtdpRelationshipPeerDeviceId=_RaisecomRtdpRelationshipPeerDeviceId_Object((1,3,6,1,4,1,8886,1,6,2,8,1,2),_RaisecomRtdpRelationshipPeerDeviceId_Type())
raisecomRtdpRelationshipPeerDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpRelationshipPeerDeviceId.setStatus(_A)
_RaisecomRtdpRelationshipNativePort_Type=Integer32
_RaisecomRtdpRelationshipNativePort_Object=MibTableColumn
raisecomRtdpRelationshipNativePort=_RaisecomRtdpRelationshipNativePort_Object((1,3,6,1,4,1,8886,1,6,2,8,1,3),_RaisecomRtdpRelationshipNativePort_Type())
raisecomRtdpRelationshipNativePort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpRelationshipNativePort.setStatus(_A)
_RaisecomRtdpRelationshipPeerPort_Type=Integer32
_RaisecomRtdpRelationshipPeerPort_Object=MibTableColumn
raisecomRtdpRelationshipPeerPort=_RaisecomRtdpRelationshipPeerPort_Object((1,3,6,1,4,1,8886,1,6,2,8,1,4),_RaisecomRtdpRelationshipPeerPort_Type())
raisecomRtdpRelationshipPeerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRtdpRelationshipPeerPort.setStatus(_A)
class _RaisecomRtdpControlVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_RaisecomRtdpControlVlan_Type.__name__=_C
_RaisecomRtdpControlVlan_Object=MibScalar
raisecomRtdpControlVlan=_RaisecomRtdpControlVlan_Object((1,3,6,1,4,1,8886,1,6,2,10),_RaisecomRtdpControlVlan_Type())
raisecomRtdpControlVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRtdpControlVlan.setStatus(_A)
_RaisecomRtdpControlVlanPorts_Type=PortList
_RaisecomRtdpControlVlanPorts_Object=MibScalar
raisecomRtdpControlVlanPorts=_RaisecomRtdpControlVlanPorts_Object((1,3,6,1,4,1,8886,1,6,2,11),_RaisecomRtdpControlVlanPorts_Type())
raisecomRtdpControlVlanPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRtdpControlVlanPorts.setStatus(_A)
raisecomRtdpTrap=NotificationType((1,3,6,1,4,1,8886,1,6,2,9))
if mibBuilder.loadTexts:raisecomRtdpTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'raisecomTopoDiscovery':raisecomTopoDiscovery,'raisecomRtdpCollectEnable':raisecomRtdpCollectEnable,'raisecomRtdpReportEnable':raisecomRtdpReportEnable,'raisecomRtdpMaxHops':raisecomRtdpMaxHops,'raisecomRtdpDeviceDiscoveryTable':raisecomRtdpDeviceDiscoveryTable,'raisecomRtdpDeviceDiscoveryEntry':raisecomRtdpDeviceDiscoveryEntry,'raisecomRtdpDeviceDiscoveryDeviceId':raisecomRtdpDeviceDiscoveryDeviceId,'raisecomRtdpDeviceDiscoveryHops':raisecomRtdpDeviceDiscoveryHops,'raisecomRtdpDeviceDiscoveryHostName':raisecomRtdpDeviceDiscoveryHostName,'raisecomRtdpDeviceDiscoveryPlatformOid':raisecomRtdpDeviceDiscoveryPlatformOid,'raisecomRtdpDeviceDiscoveryVersion':raisecomRtdpDeviceDiscoveryVersion,'raisecomRtdpDeviceDiscoveryCapabilities':raisecomRtdpDeviceDiscoveryCapabilities,'raisecomRtdpDeviceDiscoveryRole':raisecomRtdpDeviceDiscoveryRole,'raisecomRtdpDeviceDiscoveryCommanderMac':raisecomRtdpDeviceDiscoveryCommanderMac,'raisecomRtdpDeviceDiscoveryAutoActive':raisecomRtdpDeviceDiscoveryAutoActive,'raisecomRtdpDeviceDiscoveryAutoActiveMac':raisecomRtdpDeviceDiscoveryAutoActiveMac,'raisecomRtdpRelationshipTable':raisecomRtdpRelationshipTable,'raisecomRtdpRelationshipEntry':raisecomRtdpRelationshipEntry,_J:raisecomRtdpRelationshipDeviceId,_K:raisecomRtdpRelationshipPeerDeviceId,'raisecomRtdpRelationshipNativePort':raisecomRtdpRelationshipNativePort,'raisecomRtdpRelationshipPeerPort':raisecomRtdpRelationshipPeerPort,'raisecomRtdpTrap':raisecomRtdpTrap,'raisecomRtdpControlVlan':raisecomRtdpControlVlan,'raisecomRtdpControlVlanPorts':raisecomRtdpControlVlanPorts})