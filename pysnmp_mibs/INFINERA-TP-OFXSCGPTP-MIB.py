_Q='ofxScgPtpGroup'
_P='ofxScgPtpUnAssignedCarrierList'
_O='ofxScgPtpOperatingMode'
_N='ofxScgPtpCarrierCount'
_M='ofxScgPtpOpenwaveTargetTxScgPower'
_L='ofxScgPtpProvisionedPeerTp'
_K='ofxScgPtpRxPowerOffset'
_J='ofxScgPtpInstalledEncodingMode'
_I='ofxScgPtpLineSystemMode'
_H='ofxScgPtpProvEncodingMode'
_G='ofxScgPtpPowerControlLoop'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-OFXSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnEnableDisable,InfnEncoding,InfnEqptType,InfnOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnEnableDisable','InfnEncoding','InfnEqptType','InfnOperatingMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ofxScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,42))
if mibBuilder.loadTexts:ofxScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_OfxScgPtpTable_Object=MibTable
ofxScgPtpTable=_OfxScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1))
if mibBuilder.loadTexts:ofxScgPtpTable.setStatus(_A)
_OfxScgPtpEntry_Object=MibTableRow
ofxScgPtpEntry=_OfxScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1))
ofxScgPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ofxScgPtpEntry.setStatus(_A)
_OfxScgPtpPowerControlLoop_Type=InfnEnableDisable
_OfxScgPtpPowerControlLoop_Object=MibTableColumn
ofxScgPtpPowerControlLoop=_OfxScgPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,1),_OfxScgPtpPowerControlLoop_Type())
ofxScgPtpPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPowerControlLoop.setStatus(_A)
_OfxScgPtpProvEncodingMode_Type=InfnEncoding
_OfxScgPtpProvEncodingMode_Object=MibTableColumn
ofxScgPtpProvEncodingMode=_OfxScgPtpProvEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,2),_OfxScgPtpProvEncodingMode_Type())
ofxScgPtpProvEncodingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpProvEncodingMode.setStatus(_A)
class _OfxScgPtpLineSystemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('modeOcg',1),('modeOpenWave',2),('modeScg',3),('modeScgPassiveMux1',4)))
_OfxScgPtpLineSystemMode_Type.__name__=_F
_OfxScgPtpLineSystemMode_Object=MibTableColumn
ofxScgPtpLineSystemMode=_OfxScgPtpLineSystemMode_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,3),_OfxScgPtpLineSystemMode_Type())
ofxScgPtpLineSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpLineSystemMode.setStatus(_A)
_OfxScgPtpInstalledEncodingMode_Type=InfnEncoding
_OfxScgPtpInstalledEncodingMode_Object=MibTableColumn
ofxScgPtpInstalledEncodingMode=_OfxScgPtpInstalledEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,4),_OfxScgPtpInstalledEncodingMode_Type())
ofxScgPtpInstalledEncodingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpInstalledEncodingMode.setStatus(_A)
_OfxScgPtpRxPowerOffset_Type=FloatHundredths
_OfxScgPtpRxPowerOffset_Object=MibTableColumn
ofxScgPtpRxPowerOffset=_OfxScgPtpRxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,5),_OfxScgPtpRxPowerOffset_Type())
ofxScgPtpRxPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpRxPowerOffset.setStatus(_A)
_OfxScgPtpProvisionedPeerTp_Type=DisplayString
_OfxScgPtpProvisionedPeerTp_Object=MibTableColumn
ofxScgPtpProvisionedPeerTp=_OfxScgPtpProvisionedPeerTp_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,6),_OfxScgPtpProvisionedPeerTp_Type())
ofxScgPtpProvisionedPeerTp.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpProvisionedPeerTp.setStatus(_A)
_OfxScgPtpOpenwaveTargetTxScgPower_Type=FloatTenths
_OfxScgPtpOpenwaveTargetTxScgPower_Object=MibTableColumn
ofxScgPtpOpenwaveTargetTxScgPower=_OfxScgPtpOpenwaveTargetTxScgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,7),_OfxScgPtpOpenwaveTargetTxScgPower_Type())
ofxScgPtpOpenwaveTargetTxScgPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpOpenwaveTargetTxScgPower.setStatus(_A)
_OfxScgPtpCarrierCount_Type=FloatHundredths
_OfxScgPtpCarrierCount_Object=MibTableColumn
ofxScgPtpCarrierCount=_OfxScgPtpCarrierCount_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,8),_OfxScgPtpCarrierCount_Type())
ofxScgPtpCarrierCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpCarrierCount.setStatus(_A)
_OfxScgPtpOperatingMode_Type=InfnOperatingMode
_OfxScgPtpOperatingMode_Object=MibTableColumn
ofxScgPtpOperatingMode=_OfxScgPtpOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,9),_OfxScgPtpOperatingMode_Type())
ofxScgPtpOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpOperatingMode.setStatus(_A)
_OfxScgPtpUnAssignedCarrierList_Type=DisplayString
_OfxScgPtpUnAssignedCarrierList_Object=MibTableColumn
ofxScgPtpUnAssignedCarrierList=_OfxScgPtpUnAssignedCarrierList_Object((1,3,6,1,4,1,21296,2,2,2,2,42,1,1,10),_OfxScgPtpUnAssignedCarrierList_Type())
ofxScgPtpUnAssignedCarrierList.setMaxAccess('read-only')
if mibBuilder.loadTexts:ofxScgPtpUnAssignedCarrierList.setStatus(_A)
_OfxScgPtpConformance_ObjectIdentity=ObjectIdentity
ofxScgPtpConformance=_OfxScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,42,3))
_OfxScgPtpCompliances_ObjectIdentity=ObjectIdentity
ofxScgPtpCompliances=_OfxScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,42,3,1))
_OfxScgPtpGroups_ObjectIdentity=ObjectIdentity
ofxScgPtpGroups=_OfxScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,42,3,2))
ofxScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,42,3,2,1))
ofxScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ofxScgPtpGroup.setStatus(_A)
ofxScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,42,3,1,1))
ofxScgPtpCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:ofxScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofxScgPtpMIB':ofxScgPtpMIB,'ofxScgPtpTable':ofxScgPtpTable,'ofxScgPtpEntry':ofxScgPtpEntry,_G:ofxScgPtpPowerControlLoop,_H:ofxScgPtpProvEncodingMode,_I:ofxScgPtpLineSystemMode,_J:ofxScgPtpInstalledEncodingMode,_K:ofxScgPtpRxPowerOffset,_L:ofxScgPtpProvisionedPeerTp,_M:ofxScgPtpOpenwaveTargetTxScgPower,_N:ofxScgPtpCarrierCount,_O:ofxScgPtpOperatingMode,_P:ofxScgPtpUnAssignedCarrierList,'ofxScgPtpConformance':ofxScgPtpConformance,'ofxScgPtpCompliances':ofxScgPtpCompliances,'ofxScgPtpCompliance':ofxScgPtpCompliance,'ofxScgPtpGroups':ofxScgPtpGroups,_Q:ofxScgPtpGroup})