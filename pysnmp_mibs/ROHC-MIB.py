_AH='rohcContextStatisticsGroup'
_AG='rohcTimerGroup'
_AF='rohcStatisticsGroup'
_AE='rohcContextGroup'
_AD='rohcInstanceGroup'
_AC='rohcContextLastHeadersMeanSize'
_AB='rohcContextLastPacketsMeanSize'
_AA='rohcContextLastHeadersRatio'
_A9='rohcContextLastPacketsRatio'
_A8='rohcContextAllHeadersMeanSize'
_A7='rohcContextAllPacketsMeanSize'
_A6='rohcContextAllHeadersRatio'
_A5='rohcContextAllPacketsRatio'
_A4='rohcContextDecompressorRepairs'
_A3='rohcContextDecompressorFailures'
_A2='rohcContextFeedbacks'
_A1='rohcContextIRDYNs'
_A0='rohcContextIRs'
_z='rohcContextPackets'
_y='rohcContextDeactivationTime'
_x='rohcContextActivationTime'
_w='rohcContextStorageTime'
_v='rohcInstanceContextStorageTime'
_u='rohcContextDecompressorDepth'
_t='rohcContextProfile'
_s='rohcContextCIDState'
_r='rohcInstanceCompressionRatio'
_q='rohcInstanceFeedbacks'
_p='rohcInstanceIRDYNs'
_o='rohcInstanceIRs'
_n='rohcInstancePackets'
_m='rohcInstanceContextsCurrent'
_l='rohcInstanceContextsTotal'
_k='rohcProfileNegotiated'
_j='rohcProfileDescr'
_i='rohcProfileVersion'
_h='rohcProfileVendor'
_g='rohcInstanceStatus'
_f='rohcInstanceMRRU'
_e='rohcInstanceLargeCIDs'
_d='rohcInstanceMaxCID'
_c='rohcInstanceClockRes'
_b='rohcInstanceDescr'
_a='rohcInstanceVersion'
_Z='rohcInstanceVendor'
_Y='rohcInstanceFBChannelID'
_X='rohcChannelStatus'
_W='rohcChannelDescr'
_V='rohcChannelFeedbackFor'
_U='rohcChannelType'
_T='0000000000000000'
_S='rohcContextCID'
_R='rohcProfile'
_Q='centi-seconds'
_P='read-write'
_O='rohcInstanceType'
_N='disabled'
_M='enabled'
_L='TimeInterval'
_K='DateAndTime'
_J='SnmpAdminString'
_I='ifIndex'
_H='IF-MIB'
_G='not-accessible'
_F='rohcChannelID'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='ROHC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'DisplayString','PhysAddress','TextualConvention',_L,'TruthValue')
rohcMIB=ModuleIdentity((1,3,6,1,2,1,112))
if mibBuilder.loadTexts:rohcMIB.setRevisions(('2004-06-03 00:00',))
class RohcChannelIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class RohcChannelIdentifierOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class RohcCompressionRatio(TextualConvention,Unsigned32):status=_A;displayHint='d'
_RohcObjects_ObjectIdentity=ObjectIdentity
rohcObjects=_RohcObjects_ObjectIdentity((1,3,6,1,2,1,112,1))
_RohcInstanceObjects_ObjectIdentity=ObjectIdentity
rohcInstanceObjects=_RohcInstanceObjects_ObjectIdentity((1,3,6,1,2,1,112,1,1))
_RohcChannelTable_Object=MibTable
rohcChannelTable=_RohcChannelTable_Object((1,3,6,1,2,1,112,1,1,1))
if mibBuilder.loadTexts:rohcChannelTable.setStatus(_A)
_RohcChannelEntry_Object=MibTableRow
rohcChannelEntry=_RohcChannelEntry_Object((1,3,6,1,2,1,112,1,1,1,1))
rohcChannelEntry.setIndexNames((0,_H,_I),(0,_B,_F))
if mibBuilder.loadTexts:rohcChannelEntry.setStatus(_A)
_RohcChannelID_Type=RohcChannelIdentifier
_RohcChannelID_Object=MibTableColumn
rohcChannelID=_RohcChannelID_Object((1,3,6,1,2,1,112,1,1,1,1,2),_RohcChannelID_Type())
rohcChannelID.setMaxAccess(_G)
if mibBuilder.loadTexts:rohcChannelID.setStatus(_A)
class _RohcChannelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notInUse',1),('rohc',2),('dedicatedFeedback',3)))
_RohcChannelType_Type.__name__=_D
_RohcChannelType_Object=MibTableColumn
rohcChannelType=_RohcChannelType_Object((1,3,6,1,2,1,112,1,1,1,1,3),_RohcChannelType_Type())
rohcChannelType.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcChannelType.setStatus(_A)
_RohcChannelFeedbackFor_Type=RohcChannelIdentifierOrZero
_RohcChannelFeedbackFor_Object=MibTableColumn
rohcChannelFeedbackFor=_RohcChannelFeedbackFor_Object((1,3,6,1,2,1,112,1,1,1,1,4),_RohcChannelFeedbackFor_Type())
rohcChannelFeedbackFor.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcChannelFeedbackFor.setStatus(_A)
_RohcChannelDescr_Type=SnmpAdminString
_RohcChannelDescr_Object=MibTableColumn
rohcChannelDescr=_RohcChannelDescr_Object((1,3,6,1,2,1,112,1,1,1,1,5),_RohcChannelDescr_Type())
rohcChannelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcChannelDescr.setStatus(_A)
class _RohcChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_RohcChannelStatus_Type.__name__=_D
_RohcChannelStatus_Object=MibTableColumn
rohcChannelStatus=_RohcChannelStatus_Object((1,3,6,1,2,1,112,1,1,1,1,6),_RohcChannelStatus_Type())
rohcChannelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcChannelStatus.setStatus(_A)
_RohcInstanceTable_Object=MibTable
rohcInstanceTable=_RohcInstanceTable_Object((1,3,6,1,2,1,112,1,1,2))
if mibBuilder.loadTexts:rohcInstanceTable.setStatus(_A)
_RohcInstanceEntry_Object=MibTableRow
rohcInstanceEntry=_RohcInstanceEntry_Object((1,3,6,1,2,1,112,1,1,2,1))
rohcInstanceEntry.setIndexNames((0,_H,_I),(0,_B,_O),(0,_B,_F))
if mibBuilder.loadTexts:rohcInstanceEntry.setStatus(_A)
class _RohcInstanceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('compressor',1),('decompressor',2)))
_RohcInstanceType_Type.__name__=_D
_RohcInstanceType_Object=MibTableColumn
rohcInstanceType=_RohcInstanceType_Object((1,3,6,1,2,1,112,1,1,2,1,2),_RohcInstanceType_Type())
rohcInstanceType.setMaxAccess(_G)
if mibBuilder.loadTexts:rohcInstanceType.setStatus(_A)
_RohcInstanceFBChannelID_Type=RohcChannelIdentifierOrZero
_RohcInstanceFBChannelID_Object=MibTableColumn
rohcInstanceFBChannelID=_RohcInstanceFBChannelID_Object((1,3,6,1,2,1,112,1,1,2,1,4),_RohcInstanceFBChannelID_Type())
rohcInstanceFBChannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceFBChannelID.setStatus(_A)
_RohcInstanceVendor_Type=ObjectIdentifier
_RohcInstanceVendor_Object=MibTableColumn
rohcInstanceVendor=_RohcInstanceVendor_Object((1,3,6,1,2,1,112,1,1,2,1,5),_RohcInstanceVendor_Type())
rohcInstanceVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceVendor.setStatus(_A)
class _RohcInstanceVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RohcInstanceVersion_Type.__name__=_J
_RohcInstanceVersion_Object=MibTableColumn
rohcInstanceVersion=_RohcInstanceVersion_Object((1,3,6,1,2,1,112,1,1,2,1,6),_RohcInstanceVersion_Type())
rohcInstanceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceVersion.setStatus(_A)
_RohcInstanceDescr_Type=SnmpAdminString
_RohcInstanceDescr_Object=MibTableColumn
rohcInstanceDescr=_RohcInstanceDescr_Object((1,3,6,1,2,1,112,1,1,2,1,7),_RohcInstanceDescr_Type())
rohcInstanceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceDescr.setStatus(_A)
_RohcInstanceClockRes_Type=Unsigned32
_RohcInstanceClockRes_Object=MibTableColumn
rohcInstanceClockRes=_RohcInstanceClockRes_Object((1,3,6,1,2,1,112,1,1,2,1,8),_RohcInstanceClockRes_Type())
rohcInstanceClockRes.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceClockRes.setStatus(_A)
if mibBuilder.loadTexts:rohcInstanceClockRes.setUnits('milliseconds')
class _RohcInstanceMaxCID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_RohcInstanceMaxCID_Type.__name__=_E
_RohcInstanceMaxCID_Object=MibTableColumn
rohcInstanceMaxCID=_RohcInstanceMaxCID_Object((1,3,6,1,2,1,112,1,1,2,1,9),_RohcInstanceMaxCID_Type())
rohcInstanceMaxCID.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceMaxCID.setStatus(_A)
_RohcInstanceLargeCIDs_Type=TruthValue
_RohcInstanceLargeCIDs_Object=MibTableColumn
rohcInstanceLargeCIDs=_RohcInstanceLargeCIDs_Object((1,3,6,1,2,1,112,1,1,2,1,10),_RohcInstanceLargeCIDs_Type())
rohcInstanceLargeCIDs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceLargeCIDs.setStatus(_A)
_RohcInstanceMRRU_Type=Unsigned32
_RohcInstanceMRRU_Object=MibTableColumn
rohcInstanceMRRU=_RohcInstanceMRRU_Object((1,3,6,1,2,1,112,1,1,2,1,11),_RohcInstanceMRRU_Type())
rohcInstanceMRRU.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceMRRU.setStatus(_A)
class _RohcInstanceContextStorageTime_Type(TimeInterval):defaultValue=360000
_RohcInstanceContextStorageTime_Type.__name__=_L
_RohcInstanceContextStorageTime_Object=MibTableColumn
rohcInstanceContextStorageTime=_RohcInstanceContextStorageTime_Object((1,3,6,1,2,1,112,1,1,2,1,12),_RohcInstanceContextStorageTime_Type())
rohcInstanceContextStorageTime.setMaxAccess(_P)
if mibBuilder.loadTexts:rohcInstanceContextStorageTime.setStatus(_A)
if mibBuilder.loadTexts:rohcInstanceContextStorageTime.setUnits(_Q)
class _RohcInstanceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_RohcInstanceStatus_Type.__name__=_D
_RohcInstanceStatus_Object=MibTableColumn
rohcInstanceStatus=_RohcInstanceStatus_Object((1,3,6,1,2,1,112,1,1,2,1,13),_RohcInstanceStatus_Type())
rohcInstanceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceStatus.setStatus(_A)
_RohcInstanceContextsTotal_Type=Counter32
_RohcInstanceContextsTotal_Object=MibTableColumn
rohcInstanceContextsTotal=_RohcInstanceContextsTotal_Object((1,3,6,1,2,1,112,1,1,2,1,14),_RohcInstanceContextsTotal_Type())
rohcInstanceContextsTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceContextsTotal.setStatus(_A)
_RohcInstanceContextsCurrent_Type=Unsigned32
_RohcInstanceContextsCurrent_Object=MibTableColumn
rohcInstanceContextsCurrent=_RohcInstanceContextsCurrent_Object((1,3,6,1,2,1,112,1,1,2,1,15),_RohcInstanceContextsCurrent_Type())
rohcInstanceContextsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceContextsCurrent.setStatus(_A)
_RohcInstancePackets_Type=Counter32
_RohcInstancePackets_Object=MibTableColumn
rohcInstancePackets=_RohcInstancePackets_Object((1,3,6,1,2,1,112,1,1,2,1,16),_RohcInstancePackets_Type())
rohcInstancePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstancePackets.setStatus(_A)
_RohcInstanceIRs_Type=Counter32
_RohcInstanceIRs_Object=MibTableColumn
rohcInstanceIRs=_RohcInstanceIRs_Object((1,3,6,1,2,1,112,1,1,2,1,17),_RohcInstanceIRs_Type())
rohcInstanceIRs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceIRs.setStatus(_A)
_RohcInstanceIRDYNs_Type=Counter32
_RohcInstanceIRDYNs_Object=MibTableColumn
rohcInstanceIRDYNs=_RohcInstanceIRDYNs_Object((1,3,6,1,2,1,112,1,1,2,1,18),_RohcInstanceIRDYNs_Type())
rohcInstanceIRDYNs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceIRDYNs.setStatus(_A)
_RohcInstanceFeedbacks_Type=Counter32
_RohcInstanceFeedbacks_Object=MibTableColumn
rohcInstanceFeedbacks=_RohcInstanceFeedbacks_Object((1,3,6,1,2,1,112,1,1,2,1,19),_RohcInstanceFeedbacks_Type())
rohcInstanceFeedbacks.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceFeedbacks.setStatus(_A)
_RohcInstanceCompressionRatio_Type=RohcCompressionRatio
_RohcInstanceCompressionRatio_Object=MibTableColumn
rohcInstanceCompressionRatio=_RohcInstanceCompressionRatio_Object((1,3,6,1,2,1,112,1,1,2,1,20),_RohcInstanceCompressionRatio_Type())
rohcInstanceCompressionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcInstanceCompressionRatio.setStatus(_A)
_RohcProfileTable_Object=MibTable
rohcProfileTable=_RohcProfileTable_Object((1,3,6,1,2,1,112,1,1,3))
if mibBuilder.loadTexts:rohcProfileTable.setStatus(_A)
_RohcProfileEntry_Object=MibTableRow
rohcProfileEntry=_RohcProfileEntry_Object((1,3,6,1,2,1,112,1,1,3,1))
rohcProfileEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:rohcProfileEntry.setStatus(_A)
class _RohcProfile_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RohcProfile_Type.__name__=_E
_RohcProfile_Object=MibTableColumn
rohcProfile=_RohcProfile_Object((1,3,6,1,2,1,112,1,1,3,1,2),_RohcProfile_Type())
rohcProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:rohcProfile.setStatus(_A)
_RohcProfileVendor_Type=ObjectIdentifier
_RohcProfileVendor_Object=MibTableColumn
rohcProfileVendor=_RohcProfileVendor_Object((1,3,6,1,2,1,112,1,1,3,1,3),_RohcProfileVendor_Type())
rohcProfileVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcProfileVendor.setStatus(_A)
class _RohcProfileVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RohcProfileVersion_Type.__name__=_J
_RohcProfileVersion_Object=MibTableColumn
rohcProfileVersion=_RohcProfileVersion_Object((1,3,6,1,2,1,112,1,1,3,1,4),_RohcProfileVersion_Type())
rohcProfileVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcProfileVersion.setStatus(_A)
_RohcProfileDescr_Type=SnmpAdminString
_RohcProfileDescr_Object=MibTableColumn
rohcProfileDescr=_RohcProfileDescr_Object((1,3,6,1,2,1,112,1,1,3,1,5),_RohcProfileDescr_Type())
rohcProfileDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcProfileDescr.setStatus(_A)
_RohcProfileNegotiated_Type=TruthValue
_RohcProfileNegotiated_Object=MibTableColumn
rohcProfileNegotiated=_RohcProfileNegotiated_Object((1,3,6,1,2,1,112,1,1,3,1,6),_RohcProfileNegotiated_Type())
rohcProfileNegotiated.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcProfileNegotiated.setStatus(_A)
_RohcContextTable_Object=MibTable
rohcContextTable=_RohcContextTable_Object((1,3,6,1,2,1,112,1,2))
if mibBuilder.loadTexts:rohcContextTable.setStatus(_A)
_RohcContextEntry_Object=MibTableRow
rohcContextEntry=_RohcContextEntry_Object((1,3,6,1,2,1,112,1,2,1))
rohcContextEntry.setIndexNames((0,_B,_F),(0,_B,_S))
if mibBuilder.loadTexts:rohcContextEntry.setStatus(_A)
class _RohcContextCID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_RohcContextCID_Type.__name__=_E
_RohcContextCID_Object=MibTableColumn
rohcContextCID=_RohcContextCID_Object((1,3,6,1,2,1,112,1,2,1,2),_RohcContextCID_Type())
rohcContextCID.setMaxAccess(_G)
if mibBuilder.loadTexts:rohcContextCID.setStatus(_A)
class _RohcContextCIDState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unused',1),('active',2),('expired',3),('terminated',4)))
_RohcContextCIDState_Type.__name__=_D
_RohcContextCIDState_Object=MibTableColumn
rohcContextCIDState=_RohcContextCIDState_Object((1,3,6,1,2,1,112,1,2,1,3),_RohcContextCIDState_Type())
rohcContextCIDState.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextCIDState.setStatus(_A)
class _RohcContextProfile_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RohcContextProfile_Type.__name__=_E
_RohcContextProfile_Object=MibTableColumn
rohcContextProfile=_RohcContextProfile_Object((1,3,6,1,2,1,112,1,2,1,4),_RohcContextProfile_Type())
rohcContextProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextProfile.setStatus(_A)
_RohcContextDecompressorDepth_Type=Unsigned32
_RohcContextDecompressorDepth_Object=MibTableColumn
rohcContextDecompressorDepth=_RohcContextDecompressorDepth_Object((1,3,6,1,2,1,112,1,2,1,5),_RohcContextDecompressorDepth_Type())
rohcContextDecompressorDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextDecompressorDepth.setStatus(_A)
_RohcContextStorageTime_Type=TimeInterval
_RohcContextStorageTime_Object=MibTableColumn
rohcContextStorageTime=_RohcContextStorageTime_Object((1,3,6,1,2,1,112,1,2,1,6),_RohcContextStorageTime_Type())
rohcContextStorageTime.setMaxAccess(_P)
if mibBuilder.loadTexts:rohcContextStorageTime.setStatus(_A)
if mibBuilder.loadTexts:rohcContextStorageTime.setUnits(_Q)
class _RohcContextActivationTime_Type(DateAndTime):defaultHexValue=_T
_RohcContextActivationTime_Type.__name__=_K
_RohcContextActivationTime_Object=MibTableColumn
rohcContextActivationTime=_RohcContextActivationTime_Object((1,3,6,1,2,1,112,1,2,1,7),_RohcContextActivationTime_Type())
rohcContextActivationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextActivationTime.setStatus(_A)
class _RohcContextDeactivationTime_Type(DateAndTime):defaultHexValue=_T
_RohcContextDeactivationTime_Type.__name__=_K
_RohcContextDeactivationTime_Object=MibTableColumn
rohcContextDeactivationTime=_RohcContextDeactivationTime_Object((1,3,6,1,2,1,112,1,2,1,8),_RohcContextDeactivationTime_Type())
rohcContextDeactivationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextDeactivationTime.setStatus(_A)
_RohcContextPackets_Type=Counter32
_RohcContextPackets_Object=MibTableColumn
rohcContextPackets=_RohcContextPackets_Object((1,3,6,1,2,1,112,1,2,1,9),_RohcContextPackets_Type())
rohcContextPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextPackets.setStatus(_A)
_RohcContextIRs_Type=Counter32
_RohcContextIRs_Object=MibTableColumn
rohcContextIRs=_RohcContextIRs_Object((1,3,6,1,2,1,112,1,2,1,10),_RohcContextIRs_Type())
rohcContextIRs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextIRs.setStatus(_A)
_RohcContextIRDYNs_Type=Counter32
_RohcContextIRDYNs_Object=MibTableColumn
rohcContextIRDYNs=_RohcContextIRDYNs_Object((1,3,6,1,2,1,112,1,2,1,11),_RohcContextIRDYNs_Type())
rohcContextIRDYNs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextIRDYNs.setStatus(_A)
_RohcContextFeedbacks_Type=Counter32
_RohcContextFeedbacks_Object=MibTableColumn
rohcContextFeedbacks=_RohcContextFeedbacks_Object((1,3,6,1,2,1,112,1,2,1,12),_RohcContextFeedbacks_Type())
rohcContextFeedbacks.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextFeedbacks.setStatus(_A)
_RohcContextDecompressorFailures_Type=Counter32
_RohcContextDecompressorFailures_Object=MibTableColumn
rohcContextDecompressorFailures=_RohcContextDecompressorFailures_Object((1,3,6,1,2,1,112,1,2,1,13),_RohcContextDecompressorFailures_Type())
rohcContextDecompressorFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextDecompressorFailures.setStatus(_A)
_RohcContextDecompressorRepairs_Type=Counter32
_RohcContextDecompressorRepairs_Object=MibTableColumn
rohcContextDecompressorRepairs=_RohcContextDecompressorRepairs_Object((1,3,6,1,2,1,112,1,2,1,14),_RohcContextDecompressorRepairs_Type())
rohcContextDecompressorRepairs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextDecompressorRepairs.setStatus(_A)
_RohcContextAllPacketsRatio_Type=RohcCompressionRatio
_RohcContextAllPacketsRatio_Object=MibTableColumn
rohcContextAllPacketsRatio=_RohcContextAllPacketsRatio_Object((1,3,6,1,2,1,112,1,2,1,15),_RohcContextAllPacketsRatio_Type())
rohcContextAllPacketsRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextAllPacketsRatio.setStatus(_A)
_RohcContextAllHeadersRatio_Type=RohcCompressionRatio
_RohcContextAllHeadersRatio_Object=MibTableColumn
rohcContextAllHeadersRatio=_RohcContextAllHeadersRatio_Object((1,3,6,1,2,1,112,1,2,1,16),_RohcContextAllHeadersRatio_Type())
rohcContextAllHeadersRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextAllHeadersRatio.setStatus(_A)
_RohcContextAllPacketsMeanSize_Type=Unsigned32
_RohcContextAllPacketsMeanSize_Object=MibTableColumn
rohcContextAllPacketsMeanSize=_RohcContextAllPacketsMeanSize_Object((1,3,6,1,2,1,112,1,2,1,17),_RohcContextAllPacketsMeanSize_Type())
rohcContextAllPacketsMeanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextAllPacketsMeanSize.setStatus(_A)
_RohcContextAllHeadersMeanSize_Type=Unsigned32
_RohcContextAllHeadersMeanSize_Object=MibTableColumn
rohcContextAllHeadersMeanSize=_RohcContextAllHeadersMeanSize_Object((1,3,6,1,2,1,112,1,2,1,18),_RohcContextAllHeadersMeanSize_Type())
rohcContextAllHeadersMeanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextAllHeadersMeanSize.setStatus(_A)
_RohcContextLastPacketsRatio_Type=RohcCompressionRatio
_RohcContextLastPacketsRatio_Object=MibTableColumn
rohcContextLastPacketsRatio=_RohcContextLastPacketsRatio_Object((1,3,6,1,2,1,112,1,2,1,19),_RohcContextLastPacketsRatio_Type())
rohcContextLastPacketsRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextLastPacketsRatio.setStatus(_A)
_RohcContextLastHeadersRatio_Type=RohcCompressionRatio
_RohcContextLastHeadersRatio_Object=MibTableColumn
rohcContextLastHeadersRatio=_RohcContextLastHeadersRatio_Object((1,3,6,1,2,1,112,1,2,1,20),_RohcContextLastHeadersRatio_Type())
rohcContextLastHeadersRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextLastHeadersRatio.setStatus(_A)
_RohcContextLastPacketsMeanSize_Type=Unsigned32
_RohcContextLastPacketsMeanSize_Object=MibTableColumn
rohcContextLastPacketsMeanSize=_RohcContextLastPacketsMeanSize_Object((1,3,6,1,2,1,112,1,2,1,21),_RohcContextLastPacketsMeanSize_Type())
rohcContextLastPacketsMeanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextLastPacketsMeanSize.setStatus(_A)
_RohcContextLastHeadersMeanSize_Type=Unsigned32
_RohcContextLastHeadersMeanSize_Object=MibTableColumn
rohcContextLastHeadersMeanSize=_RohcContextLastHeadersMeanSize_Object((1,3,6,1,2,1,112,1,2,1,22),_RohcContextLastHeadersMeanSize_Type())
rohcContextLastHeadersMeanSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcContextLastHeadersMeanSize.setStatus(_A)
_RohcConformance_ObjectIdentity=ObjectIdentity
rohcConformance=_RohcConformance_ObjectIdentity((1,3,6,1,2,1,112,2))
_RohcCompliances_ObjectIdentity=ObjectIdentity
rohcCompliances=_RohcCompliances_ObjectIdentity((1,3,6,1,2,1,112,2,1))
_RohcGroups_ObjectIdentity=ObjectIdentity
rohcGroups=_RohcGroups_ObjectIdentity((1,3,6,1,2,1,112,2,2))
rohcInstanceGroup=ObjectGroup((1,3,6,1,2,1,112,2,2,2))
rohcInstanceGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:rohcInstanceGroup.setStatus(_A)
rohcStatisticsGroup=ObjectGroup((1,3,6,1,2,1,112,2,2,4))
rohcStatisticsGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:rohcStatisticsGroup.setStatus(_A)
rohcContextGroup=ObjectGroup((1,3,6,1,2,1,112,2,2,5))
rohcContextGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:rohcContextGroup.setStatus(_A)
rohcTimerGroup=ObjectGroup((1,3,6,1,2,1,112,2,2,6))
rohcTimerGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:rohcTimerGroup.setStatus(_A)
rohcContextStatisticsGroup=ObjectGroup((1,3,6,1,2,1,112,2,2,7))
rohcContextStatisticsGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:rohcContextStatisticsGroup.setStatus(_A)
rohcCompliance=ModuleCompliance((1,3,6,1,2,1,112,2,1,1))
rohcCompliance.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:rohcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RohcChannelIdentifier':RohcChannelIdentifier,'RohcChannelIdentifierOrZero':RohcChannelIdentifierOrZero,'RohcCompressionRatio':RohcCompressionRatio,'rohcMIB':rohcMIB,'rohcObjects':rohcObjects,'rohcInstanceObjects':rohcInstanceObjects,'rohcChannelTable':rohcChannelTable,'rohcChannelEntry':rohcChannelEntry,_F:rohcChannelID,_U:rohcChannelType,_V:rohcChannelFeedbackFor,_W:rohcChannelDescr,_X:rohcChannelStatus,'rohcInstanceTable':rohcInstanceTable,'rohcInstanceEntry':rohcInstanceEntry,_O:rohcInstanceType,_Y:rohcInstanceFBChannelID,_Z:rohcInstanceVendor,_a:rohcInstanceVersion,_b:rohcInstanceDescr,_c:rohcInstanceClockRes,_d:rohcInstanceMaxCID,_e:rohcInstanceLargeCIDs,_f:rohcInstanceMRRU,_v:rohcInstanceContextStorageTime,_g:rohcInstanceStatus,_l:rohcInstanceContextsTotal,_m:rohcInstanceContextsCurrent,_n:rohcInstancePackets,_o:rohcInstanceIRs,_p:rohcInstanceIRDYNs,_q:rohcInstanceFeedbacks,_r:rohcInstanceCompressionRatio,'rohcProfileTable':rohcProfileTable,'rohcProfileEntry':rohcProfileEntry,_R:rohcProfile,_h:rohcProfileVendor,_i:rohcProfileVersion,_j:rohcProfileDescr,_k:rohcProfileNegotiated,'rohcContextTable':rohcContextTable,'rohcContextEntry':rohcContextEntry,_S:rohcContextCID,_s:rohcContextCIDState,_t:rohcContextProfile,_u:rohcContextDecompressorDepth,_w:rohcContextStorageTime,_x:rohcContextActivationTime,_y:rohcContextDeactivationTime,_z:rohcContextPackets,_A0:rohcContextIRs,_A1:rohcContextIRDYNs,_A2:rohcContextFeedbacks,_A3:rohcContextDecompressorFailures,_A4:rohcContextDecompressorRepairs,_A5:rohcContextAllPacketsRatio,_A6:rohcContextAllHeadersRatio,_A7:rohcContextAllPacketsMeanSize,_A8:rohcContextAllHeadersMeanSize,_A9:rohcContextLastPacketsRatio,_AA:rohcContextLastHeadersRatio,_AB:rohcContextLastPacketsMeanSize,_AC:rohcContextLastHeadersMeanSize,'rohcConformance':rohcConformance,'rohcCompliances':rohcCompliances,'rohcCompliance':rohcCompliance,'rohcGroups':rohcGroups,_AD:rohcInstanceGroup,_AF:rohcStatisticsGroup,_AE:rohcContextGroup,_AG:rohcTimerGroup,_AH:rohcContextStatisticsGroup})