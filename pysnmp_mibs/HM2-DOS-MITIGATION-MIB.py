_i='hm2DosMitigationGeneralGroup'
_h='hm2DosMitigationTcpLandSup'
_g='hm2DosMitigationTcpNullScanSup'
_f='hm2DosMitigationTcpXmasSup'
_e='hm2DosMitigationLimiterRowStatus'
_d='hm2DosMitigationLimiterArpLimit'
_c='hm2DosMitigationLimiterTcpSynLimit'
_b='hm2DosMitigationArpLimitSup'
_a='hm2DosMitigationTcpSynLimitSup'
_Z='hm2DosMitigationIcmpChecksSup'
_Y='hm2DosMitigationTcpHdrChecksSup'
_X='hm2DosMitigationDropIpSrcRoute'
_W='hm2DosMitigationSMacDMac'
_V='hm2DosMitigationIcmpPacketSizeMode'
_U='hm2DosMitigationIcmpPacketSize'
_T='hm2DosMitigationIcmpFrags'
_S='hm2DosMitigationTcpSrcDstPortEqu'
_R='hm2DosMitigationTcpPrivilegedSrcPort'
_Q='hm2DosMitigationTcpOffsetEqu1'
_P='hm2DosMitigationLandAttack'
_O='hm2DosMitigationTcpMinimalHeaderSize'
_N='hm2DosMitigationTcpMinimalHeader'
_M='hm2DosMitigationTcpXmasScan'
_L='hm2DosMitigationTcpNullScan'
_K='hm2DosMitigationTcpSynFinScan'
_J='ifIndex'
_I='IF-MIB'
_H='read-create'
_G='hm2DosMitigationLimiterInterface'
_F='Unsigned32'
_E='read-only'
_D='HmEnabledStatus'
_C='read-write'
_B='HM2-DOS-MITIGATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_D,'hm2ConfigurationMibs')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hm2DosMitigationMib=ModuleIdentity((1,3,6,1,4,1,248,11,82))
if mibBuilder.loadTexts:hm2DosMitigationMib.setRevisions(('2012-09-18 00:00','2012-08-20 00:00','2012-06-06 00:00','2012-03-19 00:00'))
class DosFeatureValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hw',1),('sw',2),('noSup',3)))
_Hm2DosMitigationNotifications_ObjectIdentity=ObjectIdentity
hm2DosMitigationNotifications=_Hm2DosMitigationNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,82,0))
_Hm2DosMitigationObjects_ObjectIdentity=ObjectIdentity
hm2DosMitigationObjects=_Hm2DosMitigationObjects_ObjectIdentity((1,3,6,1,4,1,248,11,82,1))
_Hm2DosMitigationGeneralSettings_ObjectIdentity=ObjectIdentity
hm2DosMitigationGeneralSettings=_Hm2DosMitigationGeneralSettings_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1))
_Hm2DosMitigationCapabilities_ObjectIdentity=ObjectIdentity
hm2DosMitigationCapabilities=_Hm2DosMitigationCapabilities_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1,0))
_Hm2DosMitigationTcpHdrChecksSup_Type=DosFeatureValue
_Hm2DosMitigationTcpHdrChecksSup_Object=MibScalar
hm2DosMitigationTcpHdrChecksSup=_Hm2DosMitigationTcpHdrChecksSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,1),_Hm2DosMitigationTcpHdrChecksSup_Type())
hm2DosMitigationTcpHdrChecksSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationTcpHdrChecksSup.setStatus(_A)
_Hm2DosMitigationIcmpChecksSup_Type=DosFeatureValue
_Hm2DosMitigationIcmpChecksSup_Object=MibScalar
hm2DosMitigationIcmpChecksSup=_Hm2DosMitigationIcmpChecksSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,2),_Hm2DosMitigationIcmpChecksSup_Type())
hm2DosMitigationIcmpChecksSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationIcmpChecksSup.setStatus(_A)
_Hm2DosMitigationTcpSynLimitSup_Type=DosFeatureValue
_Hm2DosMitigationTcpSynLimitSup_Object=MibScalar
hm2DosMitigationTcpSynLimitSup=_Hm2DosMitigationTcpSynLimitSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,3),_Hm2DosMitigationTcpSynLimitSup_Type())
hm2DosMitigationTcpSynLimitSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationTcpSynLimitSup.setStatus(_A)
_Hm2DosMitigationArpLimitSup_Type=DosFeatureValue
_Hm2DosMitigationArpLimitSup_Object=MibScalar
hm2DosMitigationArpLimitSup=_Hm2DosMitigationArpLimitSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,4),_Hm2DosMitigationArpLimitSup_Type())
hm2DosMitigationArpLimitSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationArpLimitSup.setStatus(_A)
_Hm2DosMitigationTcpNullScanSup_Type=DosFeatureValue
_Hm2DosMitigationTcpNullScanSup_Object=MibScalar
hm2DosMitigationTcpNullScanSup=_Hm2DosMitigationTcpNullScanSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,5),_Hm2DosMitigationTcpNullScanSup_Type())
hm2DosMitigationTcpNullScanSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationTcpNullScanSup.setStatus(_A)
_Hm2DosMitigationTcpXmasSup_Type=DosFeatureValue
_Hm2DosMitigationTcpXmasSup_Object=MibScalar
hm2DosMitigationTcpXmasSup=_Hm2DosMitigationTcpXmasSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,6),_Hm2DosMitigationTcpXmasSup_Type())
hm2DosMitigationTcpXmasSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationTcpXmasSup.setStatus(_A)
_Hm2DosMitigationTcpLandSup_Type=DosFeatureValue
_Hm2DosMitigationTcpLandSup_Object=MibScalar
hm2DosMitigationTcpLandSup=_Hm2DosMitigationTcpLandSup_Object((1,3,6,1,4,1,248,11,82,1,1,0,7),_Hm2DosMitigationTcpLandSup_Type())
hm2DosMitigationTcpLandSup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationTcpLandSup.setStatus(_A)
_Hm2DosMitigationTcpHdrChecks_ObjectIdentity=ObjectIdentity
hm2DosMitigationTcpHdrChecks=_Hm2DosMitigationTcpHdrChecks_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1,1))
class _Hm2DosMitigationTcpNullScan_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpNullScan_Type.__name__=_D
_Hm2DosMitigationTcpNullScan_Object=MibScalar
hm2DosMitigationTcpNullScan=_Hm2DosMitigationTcpNullScan_Object((1,3,6,1,4,1,248,11,82,1,1,1,1),_Hm2DosMitigationTcpNullScan_Type())
hm2DosMitigationTcpNullScan.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpNullScan.setStatus(_A)
class _Hm2DosMitigationTcpXmasScan_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpXmasScan_Type.__name__=_D
_Hm2DosMitigationTcpXmasScan_Object=MibScalar
hm2DosMitigationTcpXmasScan=_Hm2DosMitigationTcpXmasScan_Object((1,3,6,1,4,1,248,11,82,1,1,1,4),_Hm2DosMitigationTcpXmasScan_Type())
hm2DosMitigationTcpXmasScan.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpXmasScan.setStatus(_A)
class _Hm2DosMitigationTcpSynFinScan_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpSynFinScan_Type.__name__=_D
_Hm2DosMitigationTcpSynFinScan_Object=MibScalar
hm2DosMitigationTcpSynFinScan=_Hm2DosMitigationTcpSynFinScan_Object((1,3,6,1,4,1,248,11,82,1,1,1,7),_Hm2DosMitigationTcpSynFinScan_Type())
hm2DosMitigationTcpSynFinScan.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpSynFinScan.setStatus(_A)
class _Hm2DosMitigationTcpMinimalHeader_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpMinimalHeader_Type.__name__=_D
_Hm2DosMitigationTcpMinimalHeader_Object=MibScalar
hm2DosMitigationTcpMinimalHeader=_Hm2DosMitigationTcpMinimalHeader_Object((1,3,6,1,4,1,248,11,82,1,1,1,10),_Hm2DosMitigationTcpMinimalHeader_Type())
hm2DosMitigationTcpMinimalHeader.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpMinimalHeader.setStatus(_A)
class _Hm2DosMitigationTcpMinimalHeaderSize_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,255))
_Hm2DosMitigationTcpMinimalHeaderSize_Type.__name__=_F
_Hm2DosMitigationTcpMinimalHeaderSize_Object=MibScalar
hm2DosMitigationTcpMinimalHeaderSize=_Hm2DosMitigationTcpMinimalHeaderSize_Object((1,3,6,1,4,1,248,11,82,1,1,1,11),_Hm2DosMitigationTcpMinimalHeaderSize_Type())
hm2DosMitigationTcpMinimalHeaderSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpMinimalHeaderSize.setStatus(_A)
class _Hm2DosMitigationLandAttack_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationLandAttack_Type.__name__=_D
_Hm2DosMitigationLandAttack_Object=MibScalar
hm2DosMitigationLandAttack=_Hm2DosMitigationLandAttack_Object((1,3,6,1,4,1,248,11,82,1,1,1,13),_Hm2DosMitigationLandAttack_Type())
hm2DosMitigationLandAttack.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationLandAttack.setStatus(_A)
class _Hm2DosMitigationTcpOffsetEqu1_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpOffsetEqu1_Type.__name__=_D
_Hm2DosMitigationTcpOffsetEqu1_Object=MibScalar
hm2DosMitigationTcpOffsetEqu1=_Hm2DosMitigationTcpOffsetEqu1_Object((1,3,6,1,4,1,248,11,82,1,1,1,14),_Hm2DosMitigationTcpOffsetEqu1_Type())
hm2DosMitigationTcpOffsetEqu1.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpOffsetEqu1.setStatus(_A)
class _Hm2DosMitigationTcpPrivilegedSrcPort_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpPrivilegedSrcPort_Type.__name__=_D
_Hm2DosMitigationTcpPrivilegedSrcPort_Object=MibScalar
hm2DosMitigationTcpPrivilegedSrcPort=_Hm2DosMitigationTcpPrivilegedSrcPort_Object((1,3,6,1,4,1,248,11,82,1,1,1,15),_Hm2DosMitigationTcpPrivilegedSrcPort_Type())
hm2DosMitigationTcpPrivilegedSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpPrivilegedSrcPort.setStatus(_A)
class _Hm2DosMitigationTcpSrcDstPortEqu_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationTcpSrcDstPortEqu_Type.__name__=_D
_Hm2DosMitigationTcpSrcDstPortEqu_Object=MibScalar
hm2DosMitigationTcpSrcDstPortEqu=_Hm2DosMitigationTcpSrcDstPortEqu_Object((1,3,6,1,4,1,248,11,82,1,1,1,16),_Hm2DosMitigationTcpSrcDstPortEqu_Type())
hm2DosMitigationTcpSrcDstPortEqu.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationTcpSrcDstPortEqu.setStatus(_A)
_Hm2DosMitigationIcmpChecks_ObjectIdentity=ObjectIdentity
hm2DosMitigationIcmpChecks=_Hm2DosMitigationIcmpChecks_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1,2))
class _Hm2DosMitigationIcmpFrags_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationIcmpFrags_Type.__name__=_D
_Hm2DosMitigationIcmpFrags_Object=MibScalar
hm2DosMitigationIcmpFrags=_Hm2DosMitigationIcmpFrags_Object((1,3,6,1,4,1,248,11,82,1,1,2,1),_Hm2DosMitigationIcmpFrags_Type())
hm2DosMitigationIcmpFrags.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationIcmpFrags.setStatus(_A)
class _Hm2DosMitigationIcmpPacketSize_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1472))
_Hm2DosMitigationIcmpPacketSize_Type.__name__=_F
_Hm2DosMitigationIcmpPacketSize_Object=MibScalar
hm2DosMitigationIcmpPacketSize=_Hm2DosMitigationIcmpPacketSize_Object((1,3,6,1,4,1,248,11,82,1,1,2,4),_Hm2DosMitigationIcmpPacketSize_Type())
hm2DosMitigationIcmpPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationIcmpPacketSize.setStatus(_A)
class _Hm2DosMitigationIcmpPacketSizeMode_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationIcmpPacketSizeMode_Type.__name__=_D
_Hm2DosMitigationIcmpPacketSizeMode_Object=MibScalar
hm2DosMitigationIcmpPacketSizeMode=_Hm2DosMitigationIcmpPacketSizeMode_Object((1,3,6,1,4,1,248,11,82,1,1,2,5),_Hm2DosMitigationIcmpPacketSizeMode_Type())
hm2DosMitigationIcmpPacketSizeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationIcmpPacketSizeMode.setStatus(_A)
class _Hm2DosMitigationIcmpSmurfAttack_Type(HmEnabledStatus):defaultValue=2
_Hm2DosMitigationIcmpSmurfAttack_Type.__name__=_D
_Hm2DosMitigationIcmpSmurfAttack_Object=MibScalar
hm2DosMitigationIcmpSmurfAttack=_Hm2DosMitigationIcmpSmurfAttack_Object((1,3,6,1,4,1,248,11,82,1,1,2,6),_Hm2DosMitigationIcmpSmurfAttack_Type())
hm2DosMitigationIcmpSmurfAttack.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationIcmpSmurfAttack.setStatus(_A)
_Hm2DosMitigationL2Checks_ObjectIdentity=ObjectIdentity
hm2DosMitigationL2Checks=_Hm2DosMitigationL2Checks_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1,3))
class _Hm2DosMitigationSMacDMac_Type(HmEnabledStatus):defaultValue=1
_Hm2DosMitigationSMacDMac_Type.__name__=_D
_Hm2DosMitigationSMacDMac_Object=MibScalar
hm2DosMitigationSMacDMac=_Hm2DosMitigationSMacDMac_Object((1,3,6,1,4,1,248,11,82,1,1,3,7),_Hm2DosMitigationSMacDMac_Type())
hm2DosMitigationSMacDMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationSMacDMac.setStatus(_A)
_Hm2DosMitigationIpHdrChecks_ObjectIdentity=ObjectIdentity
hm2DosMitigationIpHdrChecks=_Hm2DosMitigationIpHdrChecks_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,1,4))
class _Hm2DosMitigationDropIpSrcRoute_Type(HmEnabledStatus):defaultValue=1
_Hm2DosMitigationDropIpSrcRoute_Type.__name__=_D
_Hm2DosMitigationDropIpSrcRoute_Object=MibScalar
hm2DosMitigationDropIpSrcRoute=_Hm2DosMitigationDropIpSrcRoute_Object((1,3,6,1,4,1,248,11,82,1,1,4,1),_Hm2DosMitigationDropIpSrcRoute_Type())
hm2DosMitigationDropIpSrcRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DosMitigationDropIpSrcRoute.setStatus(_A)
_Hm2DosMitigationLimiter_ObjectIdentity=ObjectIdentity
hm2DosMitigationLimiter=_Hm2DosMitigationLimiter_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,2))
_Hm2DosMitigationLimiterObjects_ObjectIdentity=ObjectIdentity
hm2DosMitigationLimiterObjects=_Hm2DosMitigationLimiterObjects_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,2,1))
_Hm2DosMitigationLimiterRules_ObjectIdentity=ObjectIdentity
hm2DosMitigationLimiterRules=_Hm2DosMitigationLimiterRules_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,2,2))
_Hm2DosMitigationLimiterRuleTable_Object=MibTable
hm2DosMitigationLimiterRuleTable=_Hm2DosMitigationLimiterRuleTable_Object((1,3,6,1,4,1,248,11,82,1,2,2,1))
if mibBuilder.loadTexts:hm2DosMitigationLimiterRuleTable.setStatus(_A)
_Hm2DosMitigationLimiterRuleEntry_Object=MibTableRow
hm2DosMitigationLimiterRuleEntry=_Hm2DosMitigationLimiterRuleEntry_Object((1,3,6,1,4,1,248,11,82,1,2,2,1,1))
hm2DosMitigationLimiterRuleEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hm2DosMitigationLimiterRuleEntry.setStatus(_A)
_Hm2DosMitigationLimiterInterface_Type=InterfaceIndex
_Hm2DosMitigationLimiterInterface_Object=MibTableColumn
hm2DosMitigationLimiterInterface=_Hm2DosMitigationLimiterInterface_Object((1,3,6,1,4,1,248,11,82,1,2,2,1,1,1),_Hm2DosMitigationLimiterInterface_Type())
hm2DosMitigationLimiterInterface.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hm2DosMitigationLimiterInterface.setStatus(_A)
_Hm2DosMitigationLimiterTcpSynLimit_Type=Unsigned32
_Hm2DosMitigationLimiterTcpSynLimit_Object=MibTableColumn
hm2DosMitigationLimiterTcpSynLimit=_Hm2DosMitigationLimiterTcpSynLimit_Object((1,3,6,1,4,1,248,11,82,1,2,2,1,1,2),_Hm2DosMitigationLimiterTcpSynLimit_Type())
hm2DosMitigationLimiterTcpSynLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DosMitigationLimiterTcpSynLimit.setStatus(_A)
_Hm2DosMitigationLimiterArpLimit_Type=Unsigned32
_Hm2DosMitigationLimiterArpLimit_Object=MibTableColumn
hm2DosMitigationLimiterArpLimit=_Hm2DosMitigationLimiterArpLimit_Object((1,3,6,1,4,1,248,11,82,1,2,2,1,1,3),_Hm2DosMitigationLimiterArpLimit_Type())
hm2DosMitigationLimiterArpLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DosMitigationLimiterArpLimit.setStatus(_A)
_Hm2DosMitigationLimiterRowStatus_Type=RowStatus
_Hm2DosMitigationLimiterRowStatus_Object=MibTableColumn
hm2DosMitigationLimiterRowStatus=_Hm2DosMitigationLimiterRowStatus_Object((1,3,6,1,4,1,248,11,82,1,2,2,1,1,4),_Hm2DosMitigationLimiterRowStatus_Type())
hm2DosMitigationLimiterRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DosMitigationLimiterRowStatus.setStatus(_A)
_Hm2DosMitigationStatistics_ObjectIdentity=ObjectIdentity
hm2DosMitigationStatistics=_Hm2DosMitigationStatistics_ObjectIdentity((1,3,6,1,4,1,248,11,82,1,3))
_Hm2DosMitigationGlobalDropCounter_Type=Counter64
_Hm2DosMitigationGlobalDropCounter_Object=MibScalar
hm2DosMitigationGlobalDropCounter=_Hm2DosMitigationGlobalDropCounter_Object((1,3,6,1,4,1,248,11,82,1,3,1),_Hm2DosMitigationGlobalDropCounter_Type())
hm2DosMitigationGlobalDropCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationGlobalDropCounter.setStatus(_A)
_Hm2DosMitigationStatisticsPortTable_Object=MibTable
hm2DosMitigationStatisticsPortTable=_Hm2DosMitigationStatisticsPortTable_Object((1,3,6,1,4,1,248,11,82,1,3,2))
if mibBuilder.loadTexts:hm2DosMitigationStatisticsPortTable.setStatus(_A)
_Hm2DosMitigationStatisticsPortEntry_Object=MibTableRow
hm2DosMitigationStatisticsPortEntry=_Hm2DosMitigationStatisticsPortEntry_Object((1,3,6,1,4,1,248,11,82,1,3,2,1))
hm2DosMitigationStatisticsPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hm2DosMitigationStatisticsPortEntry.setStatus(_A)
_Hm2DosMitigationPortDropCounter_Type=Counter64
_Hm2DosMitigationPortDropCounter_Object=MibTableColumn
hm2DosMitigationPortDropCounter=_Hm2DosMitigationPortDropCounter_Object((1,3,6,1,4,1,248,11,82,1,3,2,1,1),_Hm2DosMitigationPortDropCounter_Type())
hm2DosMitigationPortDropCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DosMitigationPortDropCounter.setStatus(_A)
_Hm2DosMitigationConformance_ObjectIdentity=ObjectIdentity
hm2DosMitigationConformance=_Hm2DosMitigationConformance_ObjectIdentity((1,3,6,1,4,1,248,11,82,2))
_Hm2DosMitigationCompliances_ObjectIdentity=ObjectIdentity
hm2DosMitigationCompliances=_Hm2DosMitigationCompliances_ObjectIdentity((1,3,6,1,4,1,248,11,82,2,1))
_Hm2DosMitigationGroups_ObjectIdentity=ObjectIdentity
hm2DosMitigationGroups=_Hm2DosMitigationGroups_ObjectIdentity((1,3,6,1,4,1,248,11,82,2,2))
hm2DosMitigationGeneralGroup=ObjectGroup((1,3,6,1,4,1,248,11,82,2,2,1))
hm2DosMitigationGeneralGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_G),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:hm2DosMitigationGeneralGroup.setStatus(_A)
hm2DosMitigationCompliance=ModuleCompliance((1,3,6,1,4,1,248,11,82,2,1,1))
hm2DosMitigationCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:hm2DosMitigationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DosFeatureValue':DosFeatureValue,'hm2DosMitigationMib':hm2DosMitigationMib,'hm2DosMitigationNotifications':hm2DosMitigationNotifications,'hm2DosMitigationObjects':hm2DosMitigationObjects,'hm2DosMitigationGeneralSettings':hm2DosMitigationGeneralSettings,'hm2DosMitigationCapabilities':hm2DosMitigationCapabilities,_Y:hm2DosMitigationTcpHdrChecksSup,_Z:hm2DosMitigationIcmpChecksSup,_a:hm2DosMitigationTcpSynLimitSup,_b:hm2DosMitigationArpLimitSup,_g:hm2DosMitigationTcpNullScanSup,_f:hm2DosMitigationTcpXmasSup,_h:hm2DosMitigationTcpLandSup,'hm2DosMitigationTcpHdrChecks':hm2DosMitigationTcpHdrChecks,_L:hm2DosMitigationTcpNullScan,_M:hm2DosMitigationTcpXmasScan,_K:hm2DosMitigationTcpSynFinScan,_N:hm2DosMitigationTcpMinimalHeader,_O:hm2DosMitigationTcpMinimalHeaderSize,_P:hm2DosMitigationLandAttack,_Q:hm2DosMitigationTcpOffsetEqu1,_R:hm2DosMitigationTcpPrivilegedSrcPort,_S:hm2DosMitigationTcpSrcDstPortEqu,'hm2DosMitigationIcmpChecks':hm2DosMitigationIcmpChecks,_T:hm2DosMitigationIcmpFrags,_U:hm2DosMitigationIcmpPacketSize,_V:hm2DosMitigationIcmpPacketSizeMode,'hm2DosMitigationIcmpSmurfAttack':hm2DosMitigationIcmpSmurfAttack,'hm2DosMitigationL2Checks':hm2DosMitigationL2Checks,_W:hm2DosMitigationSMacDMac,'hm2DosMitigationIpHdrChecks':hm2DosMitigationIpHdrChecks,_X:hm2DosMitigationDropIpSrcRoute,'hm2DosMitigationLimiter':hm2DosMitigationLimiter,'hm2DosMitigationLimiterObjects':hm2DosMitigationLimiterObjects,'hm2DosMitigationLimiterRules':hm2DosMitigationLimiterRules,'hm2DosMitigationLimiterRuleTable':hm2DosMitigationLimiterRuleTable,'hm2DosMitigationLimiterRuleEntry':hm2DosMitigationLimiterRuleEntry,_G:hm2DosMitigationLimiterInterface,_c:hm2DosMitigationLimiterTcpSynLimit,_d:hm2DosMitigationLimiterArpLimit,_e:hm2DosMitigationLimiterRowStatus,'hm2DosMitigationStatistics':hm2DosMitigationStatistics,'hm2DosMitigationGlobalDropCounter':hm2DosMitigationGlobalDropCounter,'hm2DosMitigationStatisticsPortTable':hm2DosMitigationStatisticsPortTable,'hm2DosMitigationStatisticsPortEntry':hm2DosMitigationStatisticsPortEntry,'hm2DosMitigationPortDropCounter':hm2DosMitigationPortDropCounter,'hm2DosMitigationConformance':hm2DosMitigationConformance,'hm2DosMitigationCompliances':hm2DosMitigationCompliances,'hm2DosMitigationCompliance':hm2DosMitigationCompliance,'hm2DosMitigationGroups':hm2DosMitigationGroups,_i:hm2DosMitigationGeneralGroup})