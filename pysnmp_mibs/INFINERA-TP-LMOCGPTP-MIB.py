_U='lmOcgPtpGroup'
_T='lmOcgInstalledEncodingMode'
_S='lmOcgProvisionedEncodingMode'
_R='lmOcgOpenwaveTargetTxOcgPower'
_Q='lmOcgPtpProvPeerTP'
_P='lmOcgPtpLineSystemMode'
_O='lmOcgPtpChannelCount'
_N='lmOcgPtpAssocTeIntfList'
_M='lmOcgPtpDiscoveredOcgTP'
_L='lmOcgPtpProvisionedOcgTP'
_K='lmOcgPtpOcgPowerControlLoop'
_J='lmOcgPtpAutoDiscoveryState'
_I='lmOcgPtpDiscoveredRemoteTP'
_H='InfnPowerControlLoop'
_G='InfnAutoDiscoveryState'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-LMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnAutoDiscoveryState,InfnEncoding,InfnLineSystemMode,InfnModulation,InfnPowerControlLoop=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_G,'InfnEncoding','InfnLineSystemMode','InfnModulation',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
lmOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,34))
if mibBuilder.loadTexts:lmOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_LmOcgPtpTable_Object=MibTable
lmOcgPtpTable=_LmOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1))
if mibBuilder.loadTexts:lmOcgPtpTable.setStatus(_A)
_LmOcgPtpEntry_Object=MibTableRow
lmOcgPtpEntry=_LmOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1))
lmOcgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:lmOcgPtpEntry.setStatus(_A)
_LmOcgPtpDiscoveredRemoteTP_Type=DisplayString
_LmOcgPtpDiscoveredRemoteTP_Object=MibTableColumn
lmOcgPtpDiscoveredRemoteTP=_LmOcgPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,1),_LmOcgPtpDiscoveredRemoteTP_Type())
lmOcgPtpDiscoveredRemoteTP.setMaxAccess(_D)
if mibBuilder.loadTexts:lmOcgPtpDiscoveredRemoteTP.setStatus(_A)
class _LmOcgPtpAutoDiscoveryState_Type(InfnAutoDiscoveryState):defaultValue=4
_LmOcgPtpAutoDiscoveryState_Type.__name__=_G
_LmOcgPtpAutoDiscoveryState_Object=MibTableColumn
lmOcgPtpAutoDiscoveryState=_LmOcgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,2),_LmOcgPtpAutoDiscoveryState_Type())
lmOcgPtpAutoDiscoveryState.setMaxAccess(_D)
if mibBuilder.loadTexts:lmOcgPtpAutoDiscoveryState.setStatus(_A)
class _LmOcgPtpOcgPowerControlLoop_Type(InfnPowerControlLoop):defaultValue=2
_LmOcgPtpOcgPowerControlLoop_Type.__name__=_H
_LmOcgPtpOcgPowerControlLoop_Object=MibTableColumn
lmOcgPtpOcgPowerControlLoop=_LmOcgPtpOcgPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,3),_LmOcgPtpOcgPowerControlLoop_Type())
lmOcgPtpOcgPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpOcgPowerControlLoop.setStatus(_A)
_LmOcgPtpProvisionedOcgTP_Type=DisplayString
_LmOcgPtpProvisionedOcgTP_Object=MibTableColumn
lmOcgPtpProvisionedOcgTP=_LmOcgPtpProvisionedOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,4),_LmOcgPtpProvisionedOcgTP_Type())
lmOcgPtpProvisionedOcgTP.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpProvisionedOcgTP.setStatus(_A)
_LmOcgPtpDiscoveredOcgTP_Type=DisplayString
_LmOcgPtpDiscoveredOcgTP_Object=MibTableColumn
lmOcgPtpDiscoveredOcgTP=_LmOcgPtpDiscoveredOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,5),_LmOcgPtpDiscoveredOcgTP_Type())
lmOcgPtpDiscoveredOcgTP.setMaxAccess(_D)
if mibBuilder.loadTexts:lmOcgPtpDiscoveredOcgTP.setStatus(_A)
_LmOcgPtpAssocTeIntfList_Type=DisplayString
_LmOcgPtpAssocTeIntfList_Object=MibTableColumn
lmOcgPtpAssocTeIntfList=_LmOcgPtpAssocTeIntfList_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,6),_LmOcgPtpAssocTeIntfList_Type())
lmOcgPtpAssocTeIntfList.setMaxAccess(_D)
if mibBuilder.loadTexts:lmOcgPtpAssocTeIntfList.setStatus(_A)
_LmOcgPtpChannelCount_Type=FloatTenths
_LmOcgPtpChannelCount_Object=MibTableColumn
lmOcgPtpChannelCount=_LmOcgPtpChannelCount_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,7),_LmOcgPtpChannelCount_Type())
lmOcgPtpChannelCount.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpChannelCount.setStatus(_A)
_LmOcgPtpLineSystemMode_Type=InfnLineSystemMode
_LmOcgPtpLineSystemMode_Object=MibTableColumn
lmOcgPtpLineSystemMode=_LmOcgPtpLineSystemMode_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,8),_LmOcgPtpLineSystemMode_Type())
lmOcgPtpLineSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpLineSystemMode.setStatus(_A)
_LmOcgPtpProvPeerTP_Type=DisplayString
_LmOcgPtpProvPeerTP_Object=MibTableColumn
lmOcgPtpProvPeerTP=_LmOcgPtpProvPeerTP_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,9),_LmOcgPtpProvPeerTP_Type())
lmOcgPtpProvPeerTP.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgPtpProvPeerTP.setStatus(_A)
_LmOcgOpenwaveTargetTxOcgPower_Type=FloatTenths
_LmOcgOpenwaveTargetTxOcgPower_Object=MibTableColumn
lmOcgOpenwaveTargetTxOcgPower=_LmOcgOpenwaveTargetTxOcgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,10),_LmOcgOpenwaveTargetTxOcgPower_Type())
lmOcgOpenwaveTargetTxOcgPower.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgOpenwaveTargetTxOcgPower.setStatus(_A)
_LmOcgProvisionedEncodingMode_Type=InfnEncoding
_LmOcgProvisionedEncodingMode_Object=MibTableColumn
lmOcgProvisionedEncodingMode=_LmOcgProvisionedEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,11),_LmOcgProvisionedEncodingMode_Type())
lmOcgProvisionedEncodingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOcgProvisionedEncodingMode.setStatus(_A)
_LmOcgInstalledEncodingMode_Type=InfnEncoding
_LmOcgInstalledEncodingMode_Object=MibTableColumn
lmOcgInstalledEncodingMode=_LmOcgInstalledEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,34,1,1,12),_LmOcgInstalledEncodingMode_Type())
lmOcgInstalledEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lmOcgInstalledEncodingMode.setStatus(_A)
_LmOcgPtpConformance_ObjectIdentity=ObjectIdentity
lmOcgPtpConformance=_LmOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,34,3))
_LmOcgPtpCompliances_ObjectIdentity=ObjectIdentity
lmOcgPtpCompliances=_LmOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,34,3,1))
_LmOcgPtpGroups_ObjectIdentity=ObjectIdentity
lmOcgPtpGroups=_LmOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,34,3,2))
lmOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,34,3,2,1))
lmOcgPtpGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:lmOcgPtpGroup.setStatus(_A)
lmOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,34,3,1,1))
lmOcgPtpCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:lmOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmOcgPtpMIB':lmOcgPtpMIB,'lmOcgPtpTable':lmOcgPtpTable,'lmOcgPtpEntry':lmOcgPtpEntry,_I:lmOcgPtpDiscoveredRemoteTP,_J:lmOcgPtpAutoDiscoveryState,_K:lmOcgPtpOcgPowerControlLoop,_L:lmOcgPtpProvisionedOcgTP,_M:lmOcgPtpDiscoveredOcgTP,_N:lmOcgPtpAssocTeIntfList,_O:lmOcgPtpChannelCount,_P:lmOcgPtpLineSystemMode,_Q:lmOcgPtpProvPeerTP,_R:lmOcgOpenwaveTargetTxOcgPower,_S:lmOcgProvisionedEncodingMode,_T:lmOcgInstalledEncodingMode,'lmOcgPtpConformance':lmOcgPtpConformance,'lmOcgPtpCompliances':lmOcgPtpCompliances,'lmOcgPtpCompliance':lmOcgPtpCompliance,'lmOcgPtpGroups':lmOcgPtpGroups,_U:lmOcgPtpGroup})