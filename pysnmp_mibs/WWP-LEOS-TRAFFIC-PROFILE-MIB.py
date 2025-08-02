_c='wwpLeosTrafficProfileMeterPoolIndex'
_b='wwpLeosTrafficProfileStdVlanIndex'
_a='wwpLeosTrafficProfileStdPhb'
_Z='profile3'
_Y='profile2'
_X='profile1'
_W='wwpLeosTrafficProfileStdDscp'
_V='not-accessible'
_U='wwpLeosTrafficProfileStdIpPrec'
_T='wwpLeosTrafficProfileStdDot1d'
_S='leave'
_R='none'
_Q='disabled'
_P='enabled'
_O='Unsigned32'
_N='kbps'
_M='wwpLeosTrafficProfileCascadedIndx'
_L='DisplayString'
_K='wwpLeosTrafficProfileStdIndx'
_J='off'
_I='on'
_H='wwpLeosTrafficProfilePort'
_G='read-create'
_F='deprecated'
_E='WWP-LEOS-TRAFFIC-PROFILE-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosTrafficProfileMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,27))
if mibBuilder.loadTexts:wwpLeosTrafficProfileMIB.setRevisions(('2011-07-07 00:00','2011-03-27 17:00','2009-08-25 17:00','2008-11-14 17:00','2008-07-28 17:00','2008-06-28 17:00','2008-06-16 17:00','2008-06-13 17:00','2008-06-04 17:00','2008-05-21 17:00','2008-05-15 17:00','2001-04-03 17:00'))
_WwpLeosTrafficProfileObjects_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileObjects=_WwpLeosTrafficProfileObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,1))
_WwpLeosTrafficProfile_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfile=_WwpLeosTrafficProfile_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,1,1))
_WwpLeosTrafficProfileGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileGlobalAttrs=_WwpLeosTrafficProfileGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,1,1,1))
class _WwpLeosTrafficProfileGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosTrafficProfileGlobalState_Type.__name__=_B
_WwpLeosTrafficProfileGlobalState_Object=MibScalar
wwpLeosTrafficProfileGlobalState=_WwpLeosTrafficProfileGlobalState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,1,1),_WwpLeosTrafficProfileGlobalState_Type())
wwpLeosTrafficProfileGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileGlobalState.setStatus(_A)
class _WwpLeosTrafficProfileGlobalMeterProvisioningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pir',1),('eir',2)))
_WwpLeosTrafficProfileGlobalMeterProvisioningState_Type.__name__=_B
_WwpLeosTrafficProfileGlobalMeterProvisioningState_Object=MibScalar
wwpLeosTrafficProfileGlobalMeterProvisioningState=_WwpLeosTrafficProfileGlobalMeterProvisioningState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,1,2),_WwpLeosTrafficProfileGlobalMeterProvisioningState_Type())
wwpLeosTrafficProfileGlobalMeterProvisioningState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileGlobalMeterProvisioningState.setStatus(_A)
_WwpLeosTrafficProfilePortTable_Object=MibTable
wwpLeosTrafficProfilePortTable=_WwpLeosTrafficProfilePortTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2))
if mibBuilder.loadTexts:wwpLeosTrafficProfilePortTable.setStatus(_A)
_WwpLeosTrafficProfilePortEntry_Object=MibTableRow
wwpLeosTrafficProfilePortEntry=_WwpLeosTrafficProfilePortEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1))
wwpLeosTrafficProfilePortEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosTrafficProfilePortEntry.setStatus(_A)
class _WwpLeosTrafficProfilePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosTrafficProfilePort_Type.__name__=_B
_WwpLeosTrafficProfilePort_Object=MibTableColumn
wwpLeosTrafficProfilePort=_WwpLeosTrafficProfilePort_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,1),_WwpLeosTrafficProfilePort_Type())
wwpLeosTrafficProfilePort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfilePort.setStatus(_A)
class _WwpLeosTrafficProfileAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosTrafficProfileAdminState_Type.__name__=_B
_WwpLeosTrafficProfileAdminState_Object=MibTableColumn
wwpLeosTrafficProfileAdminState=_WwpLeosTrafficProfileAdminState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,2),_WwpLeosTrafficProfileAdminState_Type())
wwpLeosTrafficProfileAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileAdminState.setStatus(_A)
class _WwpLeosTrafficProfileOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosTrafficProfileOperState_Type.__name__=_B
_WwpLeosTrafficProfileOperState_Object=MibTableColumn
wwpLeosTrafficProfileOperState=_WwpLeosTrafficProfileOperState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,3),_WwpLeosTrafficProfileOperState_Type())
wwpLeosTrafficProfileOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileOperState.setStatus(_A)
class _WwpLeosTrafficProfileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('cascadedDot1dPri',1),('cascadedDscp',2),('cascadedIpPrec',3),('stdDot1',4),('stdDiffServ',5),('stdIpPrec',6),('stdVlan',7),('stdDscp',8),('stdVlanDot1DPri',9),('stdVlanIpp',10),('stdVlanDscp',11),('hierarchicalVlan',12),('hierarchicalPort',13),(_R,14),('advanced',15)))
_WwpLeosTrafficProfileMode_Type.__name__=_B
_WwpLeosTrafficProfileMode_Object=MibTableColumn
wwpLeosTrafficProfileMode=_WwpLeosTrafficProfileMode_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,4),_WwpLeosTrafficProfileMode_Type())
wwpLeosTrafficProfileMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMode.setStatus(_A)
class _WwpLeosTrafficProfileNonConformCascadedProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('drop',0),(_X,1),(_Y,2),(_Z,3),(_F,4)))
_WwpLeosTrafficProfileNonConformCascadedProfile_Type.__name__=_B
_WwpLeosTrafficProfileNonConformCascadedProfile_Object=MibTableColumn
wwpLeosTrafficProfileNonConformCascadedProfile=_WwpLeosTrafficProfileNonConformCascadedProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,5),_WwpLeosTrafficProfileNonConformCascadedProfile_Type())
wwpLeosTrafficProfileNonConformCascadedProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileNonConformCascadedProfile.setStatus(_F)
class _WwpLeosTrafficProfileNonConformStdProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosTrafficProfileNonConformStdProfile_Type.__name__=_B
_WwpLeosTrafficProfileNonConformStdProfile_Object=MibTableColumn
wwpLeosTrafficProfileNonConformStdProfile=_WwpLeosTrafficProfileNonConformStdProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,6),_WwpLeosTrafficProfileNonConformStdProfile_Type())
wwpLeosTrafficProfileNonConformStdProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileNonConformStdProfile.setStatus(_A)
class _WwpLeosTrafficProfileArpCascadedProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('bypass',0),(_X,1),(_Y,2),(_Z,3),(_F,4)))
_WwpLeosTrafficProfileArpCascadedProfile_Type.__name__=_B
_WwpLeosTrafficProfileArpCascadedProfile_Object=MibTableColumn
wwpLeosTrafficProfileArpCascadedProfile=_WwpLeosTrafficProfileArpCascadedProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,7),_WwpLeosTrafficProfileArpCascadedProfile_Type())
wwpLeosTrafficProfileArpCascadedProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileArpCascadedProfile.setStatus(_F)
class _WwpLeosTrafficProfileArpStdProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosTrafficProfileArpStdProfile_Type.__name__=_B
_WwpLeosTrafficProfileArpStdProfile_Object=MibTableColumn
wwpLeosTrafficProfileArpStdProfile=_WwpLeosTrafficProfileArpStdProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,8),_WwpLeosTrafficProfileArpStdProfile_Type())
wwpLeosTrafficProfileArpStdProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileArpStdProfile.setStatus(_A)
class _WwpLeosTrafficProfileMeterPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WwpLeosTrafficProfileMeterPool_Type.__name__=_B
_WwpLeosTrafficProfileMeterPool_Object=MibTableColumn
wwpLeosTrafficProfileMeterPool=_WwpLeosTrafficProfileMeterPool_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,9),_WwpLeosTrafficProfileMeterPool_Type())
wwpLeosTrafficProfileMeterPool.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPool.setStatus(_A)
class _WwpLeosTrafficProfileClassifierMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('narrow',1),('wide',2)))
_WwpLeosTrafficProfileClassifierMode_Type.__name__=_B
_WwpLeosTrafficProfileClassifierMode_Object=MibTableColumn
wwpLeosTrafficProfileClassifierMode=_WwpLeosTrafficProfileClassifierMode_Object((1,3,6,1,4,1,6141,2,60,27,1,1,2,1,10),_WwpLeosTrafficProfileClassifierMode_Type())
wwpLeosTrafficProfileClassifierMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileClassifierMode.setStatus(_A)
_WwpLeosTrafficProfileCascadedTable_Object=MibTable
wwpLeosTrafficProfileCascadedTable=_WwpLeosTrafficProfileCascadedTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTable.setStatus(_F)
_WwpLeosTrafficProfileCascadedEntry_Object=MibTableRow
wwpLeosTrafficProfileCascadedEntry=_WwpLeosTrafficProfileCascadedEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3,1))
wwpLeosTrafficProfileCascadedEntry.setIndexNames((0,_E,_H),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedEntry.setStatus(_F)
class _WwpLeosTrafficProfileCascadedIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_WwpLeosTrafficProfileCascadedIndx_Type.__name__=_B
_WwpLeosTrafficProfileCascadedIndx_Object=MibTableColumn
wwpLeosTrafficProfileCascadedIndx=_WwpLeosTrafficProfileCascadedIndx_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3,1,1),_WwpLeosTrafficProfileCascadedIndx_Type())
wwpLeosTrafficProfileCascadedIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedIndx.setStatus(_F)
_WwpLeosTrafficProfileCascadedCir_Type=Integer32
_WwpLeosTrafficProfileCascadedCir_Object=MibTableColumn
wwpLeosTrafficProfileCascadedCir=_WwpLeosTrafficProfileCascadedCir_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3,1,2),_WwpLeosTrafficProfileCascadedCir_Type())
wwpLeosTrafficProfileCascadedCir.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedCir.setStatus(_F)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedCir.setUnits(_N)
_WwpLeosTrafficProfileCascadedPir_Type=Integer32
_WwpLeosTrafficProfileCascadedPir_Object=MibTableColumn
wwpLeosTrafficProfileCascadedPir=_WwpLeosTrafficProfileCascadedPir_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3,1,3),_WwpLeosTrafficProfileCascadedPir_Type())
wwpLeosTrafficProfileCascadedPir.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedPir.setStatus(_F)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedPir.setUnits(_N)
_WwpLeosTrafficProfileCascadedStatus_Type=RowStatus
_WwpLeosTrafficProfileCascadedStatus_Object=MibTableColumn
wwpLeosTrafficProfileCascadedStatus=_WwpLeosTrafficProfileCascadedStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,3,1,5),_WwpLeosTrafficProfileCascadedStatus_Type())
wwpLeosTrafficProfileCascadedStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedStatus.setStatus(_F)
_WwpLeosTrafficProfileStdTable_Object=MibTable
wwpLeosTrafficProfileStdTable=_WwpLeosTrafficProfileStdTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTable.setStatus(_A)
_WwpLeosTrafficProfileStdEntry_Object=MibTableRow
wwpLeosTrafficProfileStdEntry=_WwpLeosTrafficProfileStdEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1))
wwpLeosTrafficProfileStdEntry.setIndexNames((0,_E,_H),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosTrafficProfileStdIndx_Type.__name__=_B
_WwpLeosTrafficProfileStdIndx_Object=MibTableColumn
wwpLeosTrafficProfileStdIndx=_WwpLeosTrafficProfileStdIndx_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,1),_WwpLeosTrafficProfileStdIndx_Type())
wwpLeosTrafficProfileStdIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIndx.setStatus(_A)
_WwpLeosTrafficProfileStdCir_Type=Integer32
_WwpLeosTrafficProfileStdCir_Object=MibTableColumn
wwpLeosTrafficProfileStdCir=_WwpLeosTrafficProfileStdCir_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,2),_WwpLeosTrafficProfileStdCir_Type())
wwpLeosTrafficProfileStdCir.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdCir.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdCir.setUnits(_N)
_WwpLeosTrafficProfileStdPir_Type=Integer32
_WwpLeosTrafficProfileStdPir_Object=MibTableColumn
wwpLeosTrafficProfileStdPir=_WwpLeosTrafficProfileStdPir_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,3),_WwpLeosTrafficProfileStdPir_Type())
wwpLeosTrafficProfileStdPir.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPir.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPir.setUnits(_N)
class _WwpLeosTrafficProfileStdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeosTrafficProfileStdName_Type.__name__=_L
_WwpLeosTrafficProfileStdName_Object=MibTableColumn
wwpLeosTrafficProfileStdName=_WwpLeosTrafficProfileStdName_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,4),_WwpLeosTrafficProfileStdName_Type())
wwpLeosTrafficProfileStdName.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdName.setStatus(_A)
_WwpLeosTrafficProfileStdStatus_Type=RowStatus
_WwpLeosTrafficProfileStdStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdStatus=_WwpLeosTrafficProfileStdStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,5),_WwpLeosTrafficProfileStdStatus_Type())
wwpLeosTrafficProfileStdStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdStatus.setStatus(_A)
class _WwpLeosTrafficProfileStdVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosTrafficProfileStdVlan_Type.__name__=_B
_WwpLeosTrafficProfileStdVlan_Object=MibTableColumn
wwpLeosTrafficProfileStdVlan=_WwpLeosTrafficProfileStdVlan_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,6),_WwpLeosTrafficProfileStdVlan_Type())
wwpLeosTrafficProfileStdVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlan.setStatus(_A)
class _WwpLeosTrafficProfileStdCbs_Type(Unsigned32):defaultValue=2
_WwpLeosTrafficProfileStdCbs_Type.__name__=_O
_WwpLeosTrafficProfileStdCbs_Object=MibTableColumn
wwpLeosTrafficProfileStdCbs=_WwpLeosTrafficProfileStdCbs_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,7),_WwpLeosTrafficProfileStdCbs_Type())
wwpLeosTrafficProfileStdCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdCbs.setStatus(_A)
class _WwpLeosTrafficProfileStdEbs_Type(Unsigned32):defaultValue=2
_WwpLeosTrafficProfileStdEbs_Type.__name__=_O
_WwpLeosTrafficProfileStdEbs_Object=MibTableColumn
wwpLeosTrafficProfileStdEbs=_WwpLeosTrafficProfileStdEbs_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,8),_WwpLeosTrafficProfileStdEbs_Type())
wwpLeosTrafficProfileStdEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdEbs.setStatus(_A)
class _WwpLeosTrafficProfileStdDscpRemarkPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('fixed',2)))
_WwpLeosTrafficProfileStdDscpRemarkPolicy_Type.__name__=_B
_WwpLeosTrafficProfileStdDscpRemarkPolicy_Object=MibTableColumn
wwpLeosTrafficProfileStdDscpRemarkPolicy=_WwpLeosTrafficProfileStdDscpRemarkPolicy_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,9),_WwpLeosTrafficProfileStdDscpRemarkPolicy_Type())
wwpLeosTrafficProfileStdDscpRemarkPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscpRemarkPolicy.setStatus(_A)
class _WwpLeosTrafficProfileStdFixedDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTrafficProfileStdFixedDscp_Type.__name__=_B
_WwpLeosTrafficProfileStdFixedDscp_Object=MibTableColumn
wwpLeosTrafficProfileStdFixedDscp=_WwpLeosTrafficProfileStdFixedDscp_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,10),_WwpLeosTrafficProfileStdFixedDscp_Type())
wwpLeosTrafficProfileStdFixedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdFixedDscp.setStatus(_A)
class _WwpLeosTrafficProfileStdUnsetVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),('unset',1)))
_WwpLeosTrafficProfileStdUnsetVlan_Type.__name__=_B
_WwpLeosTrafficProfileStdUnsetVlan_Object=MibTableColumn
wwpLeosTrafficProfileStdUnsetVlan=_WwpLeosTrafficProfileStdUnsetVlan_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,11),_WwpLeosTrafficProfileStdUnsetVlan_Type())
wwpLeosTrafficProfileStdUnsetVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdUnsetVlan.setStatus(_A)
class _WwpLeosTrafficProfileStdDefaultProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_WwpLeosTrafficProfileStdDefaultProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdDefaultProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdDefaultProfile=_WwpLeosTrafficProfileStdDefaultProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,12),_WwpLeosTrafficProfileStdDefaultProfile_Type())
wwpLeosTrafficProfileStdDefaultProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDefaultProfile.setStatus(_A)
class _WwpLeosTrafficeProfileStdDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_WwpLeosTrafficeProfileStdDrop_Type.__name__=_B
_WwpLeosTrafficeProfileStdDrop_Object=MibTableColumn
wwpLeosTrafficeProfileStdDrop=_WwpLeosTrafficeProfileStdDrop_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,13),_WwpLeosTrafficeProfileStdDrop_Type())
wwpLeosTrafficeProfileStdDrop.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficeProfileStdDrop.setStatus(_A)
_WwpLeosTrafficProfileStdParentIndex_Type=Integer32
_WwpLeosTrafficProfileStdParentIndex_Object=MibTableColumn
wwpLeosTrafficProfileStdParentIndex=_WwpLeosTrafficProfileStdParentIndex_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,14),_WwpLeosTrafficProfileStdParentIndex_Type())
wwpLeosTrafficProfileStdParentIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdParentIndex.setStatus(_A)
class _WwpLeosTrafficProfileStdChildMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('dot1dPri',1),('ipprec',2),('dscp',3),('vlan',4),('vlanCos',5),(_R,99)))
_WwpLeosTrafficProfileStdChildMode_Type.__name__=_B
_WwpLeosTrafficProfileStdChildMode_Object=MibTableColumn
wwpLeosTrafficProfileStdChildMode=_WwpLeosTrafficProfileStdChildMode_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,15),_WwpLeosTrafficProfileStdChildMode_Type())
wwpLeosTrafficProfileStdChildMode.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdChildMode.setStatus(_A)
class _WwpLeosTrafficProfileStdStatsMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileStdStatsMonitor_Type.__name__=_B
_WwpLeosTrafficProfileStdStatsMonitor_Object=MibTableColumn
wwpLeosTrafficProfileStdStatsMonitor=_WwpLeosTrafficProfileStdStatsMonitor_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,16),_WwpLeosTrafficProfileStdStatsMonitor_Type())
wwpLeosTrafficProfileStdStatsMonitor.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdStatsMonitor.setStatus(_A)
class _WwpLeosTrafficProfileStdUntaggedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileStdUntaggedState_Type.__name__=_B
_WwpLeosTrafficProfileStdUntaggedState_Object=MibTableColumn
wwpLeosTrafficProfileStdUntaggedState=_WwpLeosTrafficProfileStdUntaggedState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,17),_WwpLeosTrafficProfileStdUntaggedState_Type())
wwpLeosTrafficProfileStdUntaggedState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdUntaggedState.setStatus(_A)
class _WwpLeosTrafficProfileStdVs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeosTrafficProfileStdVs_Type.__name__=_L
_WwpLeosTrafficProfileStdVs_Object=MibTableColumn
wwpLeosTrafficProfileStdVs=_WwpLeosTrafficProfileStdVs_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,18),_WwpLeosTrafficProfileStdVs_Type())
wwpLeosTrafficProfileStdVs.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVs.setStatus(_A)
class _WwpLeosTrafficProfileStdRemarkColorPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('yellowRemarkToGreen',2),('greenRemarkToYellow',3)))
_WwpLeosTrafficProfileStdRemarkColorPolicy_Type.__name__=_B
_WwpLeosTrafficProfileStdRemarkColorPolicy_Object=MibTableColumn
wwpLeosTrafficProfileStdRemarkColorPolicy=_WwpLeosTrafficProfileStdRemarkColorPolicy_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,19),_WwpLeosTrafficProfileStdRemarkColorPolicy_Type())
wwpLeosTrafficProfileStdRemarkColorPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdRemarkColorPolicy.setStatus(_A)
class _WwpLeosTrafficProfileStdRemarkRcosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('remarkGreen',2),('remarkYellow',3),('remarkBoth',4)))
_WwpLeosTrafficProfileStdRemarkRcosPolicy_Type.__name__=_B
_WwpLeosTrafficProfileStdRemarkRcosPolicy_Object=MibTableColumn
wwpLeosTrafficProfileStdRemarkRcosPolicy=_WwpLeosTrafficProfileStdRemarkRcosPolicy_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,20),_WwpLeosTrafficProfileStdRemarkRcosPolicy_Type())
wwpLeosTrafficProfileStdRemarkRcosPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdRemarkRcosPolicy.setStatus(_A)
class _WwpLeosTrafficProfileStdYellowRemarkRcos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTrafficProfileStdYellowRemarkRcos_Type.__name__=_B
_WwpLeosTrafficProfileStdYellowRemarkRcos_Object=MibTableColumn
wwpLeosTrafficProfileStdYellowRemarkRcos=_WwpLeosTrafficProfileStdYellowRemarkRcos_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,21),_WwpLeosTrafficProfileStdYellowRemarkRcos_Type())
wwpLeosTrafficProfileStdYellowRemarkRcos.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdYellowRemarkRcos.setStatus(_A)
class _WwpLeosTrafficProfileStdGreenRemarkRcos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTrafficProfileStdGreenRemarkRcos_Type.__name__=_B
_WwpLeosTrafficProfileStdGreenRemarkRcos_Object=MibTableColumn
wwpLeosTrafficProfileStdGreenRemarkRcos=_WwpLeosTrafficProfileStdGreenRemarkRcos_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,22),_WwpLeosTrafficProfileStdGreenRemarkRcos_Type())
wwpLeosTrafficProfileStdGreenRemarkRcos.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdGreenRemarkRcos.setStatus(_A)
class _WwpLeosTrafficProfileStdIngressColorAware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileStdIngressColorAware_Type.__name__=_B
_WwpLeosTrafficProfileStdIngressColorAware_Object=MibTableColumn
wwpLeosTrafficProfileStdIngressColorAware=_WwpLeosTrafficProfileStdIngressColorAware_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,23),_WwpLeosTrafficProfileStdIngressColorAware_Type())
wwpLeosTrafficProfileStdIngressColorAware.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIngressColorAware.setStatus(_A)
_WwpLeosTrafficProfileStdEir_Type=Integer32
_WwpLeosTrafficProfileStdEir_Object=MibTableColumn
wwpLeosTrafficProfileStdEir=_WwpLeosTrafficProfileStdEir_Object((1,3,6,1,4,1,6141,2,60,27,1,1,4,1,24),_WwpLeosTrafficProfileStdEir_Type())
wwpLeosTrafficProfileStdEir.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdEir.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdEir.setUnits(_N)
_WwpLeosTrafficProfileStdDot1dTable_Object=MibTable
wwpLeosTrafficProfileStdDot1dTable=_WwpLeosTrafficProfileStdDot1dTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,5))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDot1dTable.setStatus(_A)
_WwpLeosTrafficProfileStdDot1dEntry_Object=MibTableRow
wwpLeosTrafficProfileStdDot1dEntry=_WwpLeosTrafficProfileStdDot1dEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,5,1))
wwpLeosTrafficProfileStdDot1dEntry.setIndexNames((0,_E,_H),(0,_E,_T))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDot1dEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdDot1d_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTrafficProfileStdDot1d_Type.__name__=_B
_WwpLeosTrafficProfileStdDot1d_Object=MibTableColumn
wwpLeosTrafficProfileStdDot1d=_WwpLeosTrafficProfileStdDot1d_Object((1,3,6,1,4,1,6141,2,60,27,1,1,5,1,1),_WwpLeosTrafficProfileStdDot1d_Type())
wwpLeosTrafficProfileStdDot1d.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDot1d.setStatus(_A)
class _WwpLeosTrafficProfileStdDot1dToProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosTrafficProfileStdDot1dToProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdDot1dToProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdDot1dToProfile=_WwpLeosTrafficProfileStdDot1dToProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,5,1,2),_WwpLeosTrafficProfileStdDot1dToProfile_Type())
wwpLeosTrafficProfileStdDot1dToProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDot1dToProfile.setStatus(_A)
_WwpLeosTrafficProfileStdDot1dStatus_Type=RowStatus
_WwpLeosTrafficProfileStdDot1dStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdDot1dStatus=_WwpLeosTrafficProfileStdDot1dStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,5,1,3),_WwpLeosTrafficProfileStdDot1dStatus_Type())
wwpLeosTrafficProfileStdDot1dStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDot1dStatus.setStatus(_A)
_WwpLeosTrafficProfileStdIpPrecTable_Object=MibTable
wwpLeosTrafficProfileStdIpPrecTable=_WwpLeosTrafficProfileStdIpPrecTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,6))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIpPrecTable.setStatus(_A)
_WwpLeosTrafficProfileStdIpPrecEntry_Object=MibTableRow
wwpLeosTrafficProfileStdIpPrecEntry=_WwpLeosTrafficProfileStdIpPrecEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,6,1))
wwpLeosTrafficProfileStdIpPrecEntry.setIndexNames((0,_E,_H),(0,_E,_U))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIpPrecEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdIpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTrafficProfileStdIpPrec_Type.__name__=_B
_WwpLeosTrafficProfileStdIpPrec_Object=MibTableColumn
wwpLeosTrafficProfileStdIpPrec=_WwpLeosTrafficProfileStdIpPrec_Object((1,3,6,1,4,1,6141,2,60,27,1,1,6,1,1),_WwpLeosTrafficProfileStdIpPrec_Type())
wwpLeosTrafficProfileStdIpPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIpPrec.setStatus(_A)
class _WwpLeosTrafficProfileStdIpPrecToProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosTrafficProfileStdIpPrecToProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdIpPrecToProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdIpPrecToProfile=_WwpLeosTrafficProfileStdIpPrecToProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,6,1,2),_WwpLeosTrafficProfileStdIpPrecToProfile_Type())
wwpLeosTrafficProfileStdIpPrecToProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIpPrecToProfile.setStatus(_A)
_WwpLeosTrafficProfileStdIpPrecStatus_Type=RowStatus
_WwpLeosTrafficProfileStdIpPrecStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdIpPrecStatus=_WwpLeosTrafficProfileStdIpPrecStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,6,1,3),_WwpLeosTrafficProfileStdIpPrecStatus_Type())
wwpLeosTrafficProfileStdIpPrecStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdIpPrecStatus.setStatus(_A)
_WwpLeosTrafficProfileStdPhbTable_Object=MibTable
wwpLeosTrafficProfileStdPhbTable=_WwpLeosTrafficProfileStdPhbTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,7))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPhbTable.setStatus(_A)
_WwpLeosTrafficProfileStdPhbEntry_Object=MibTableRow
wwpLeosTrafficProfileStdPhbEntry=_WwpLeosTrafficProfileStdPhbEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,7,1))
wwpLeosTrafficProfileStdPhbEntry.setIndexNames((0,_E,_H),(0,_E,_a))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPhbEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdPhb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('cs0',1),('cs1',2),('cs2',3),('cs3',4),('cs4',5),('cs5',6),('cs6',7),('cs7',8),('af1',9),('af2',10),('af3',11),('af4',12),('ef',13)))
_WwpLeosTrafficProfileStdPhb_Type.__name__=_B
_WwpLeosTrafficProfileStdPhb_Object=MibTableColumn
wwpLeosTrafficProfileStdPhb=_WwpLeosTrafficProfileStdPhb_Object((1,3,6,1,4,1,6141,2,60,27,1,1,7,1,1),_WwpLeosTrafficProfileStdPhb_Type())
wwpLeosTrafficProfileStdPhb.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPhb.setStatus(_A)
class _WwpLeosTrafficProfileStdPhbToProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_WwpLeosTrafficProfileStdPhbToProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdPhbToProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdPhbToProfile=_WwpLeosTrafficProfileStdPhbToProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,7,1,2),_WwpLeosTrafficProfileStdPhbToProfile_Type())
wwpLeosTrafficProfileStdPhbToProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPhbToProfile.setStatus(_A)
_WwpLeosTrafficProfileStdPhbStatus_Type=RowStatus
_WwpLeosTrafficProfileStdPhbStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdPhbStatus=_WwpLeosTrafficProfileStdPhbStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,7,1,3),_WwpLeosTrafficProfileStdPhbStatus_Type())
wwpLeosTrafficProfileStdPhbStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdPhbStatus.setStatus(_A)
_WwpLeosTrafficProfileCascadedStatsTable_Object=MibTable
wwpLeosTrafficProfileCascadedStatsTable=_WwpLeosTrafficProfileCascadedStatsTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedStatsTable.setStatus(_F)
_WwpLeosTrafficProfileCascadedStatsEntry_Object=MibTableRow
wwpLeosTrafficProfileCascadedStatsEntry=_WwpLeosTrafficProfileCascadedStatsEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1))
wwpLeosTrafficProfileCascadedStatsEntry.setIndexNames((0,_E,_H),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedStatsEntry.setStatus(_F)
_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedAcceptedBytesHi=_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,1),_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Type())
wwpLeosTrafficProfileCascadedAcceptedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedAcceptedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedAcceptedBytesLo=_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,2),_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Type())
wwpLeosTrafficProfileCascadedAcceptedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedAcceptedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileCascadedDroppedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedDroppedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedDroppedBytesHi=_WwpLeosTrafficProfileCascadedDroppedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,3),_WwpLeosTrafficProfileCascadedDroppedBytesHi_Type())
wwpLeosTrafficProfileCascadedDroppedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedDroppedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedDroppedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedDroppedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedDroppedBytesLo=_WwpLeosTrafficProfileCascadedDroppedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,4),_WwpLeosTrafficProfileCascadedDroppedBytesLo_Type())
wwpLeosTrafficProfileCascadedDroppedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedDroppedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedRemarkedBytesHi=_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,5),_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Type())
wwpLeosTrafficProfileCascadedRemarkedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedRemarkedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedRemarkedBytesLo=_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,8,1,6),_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Type())
wwpLeosTrafficProfileCascadedRemarkedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedRemarkedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileStdStatsTable_Object=MibTable
wwpLeosTrafficProfileStdStatsTable=_WwpLeosTrafficProfileStdStatsTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdStatsTable.setStatus(_A)
_WwpLeosTrafficProfileStdStatsEntry_Object=MibTableRow
wwpLeosTrafficProfileStdStatsEntry=_WwpLeosTrafficProfileStdStatsEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1))
wwpLeosTrafficProfileStdStatsEntry.setIndexNames((0,_E,_H),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdStatsEntry.setStatus(_A)
_WwpLeosTrafficProfileStdAcceptedBytesHi_Type=Counter32
_WwpLeosTrafficProfileStdAcceptedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileStdAcceptedBytesHi=_WwpLeosTrafficProfileStdAcceptedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,1),_WwpLeosTrafficProfileStdAcceptedBytesHi_Type())
wwpLeosTrafficProfileStdAcceptedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdAcceptedBytesHi.setStatus(_A)
_WwpLeosTrafficProfileStdAcceptedBytesLo_Type=Counter32
_WwpLeosTrafficProfileStdAcceptedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileStdAcceptedBytesLo=_WwpLeosTrafficProfileStdAcceptedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,2),_WwpLeosTrafficProfileStdAcceptedBytesLo_Type())
wwpLeosTrafficProfileStdAcceptedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdAcceptedBytesLo.setStatus(_A)
_WwpLeosTrafficProfileStdDroppedBytesHi_Type=Counter32
_WwpLeosTrafficProfileStdDroppedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileStdDroppedBytesHi=_WwpLeosTrafficProfileStdDroppedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,3),_WwpLeosTrafficProfileStdDroppedBytesHi_Type())
wwpLeosTrafficProfileStdDroppedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDroppedBytesHi.setStatus(_A)
_WwpLeosTrafficProfileStdDroppedBytesLo_Type=Counter32
_WwpLeosTrafficProfileStdDroppedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileStdDroppedBytesLo=_WwpLeosTrafficProfileStdDroppedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,4),_WwpLeosTrafficProfileStdDroppedBytesLo_Type())
wwpLeosTrafficProfileStdDroppedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDroppedBytesLo.setStatus(_A)
_WwpLeosTrafficProfileStdHCAcceptedBytes_Type=Counter64
_WwpLeosTrafficProfileStdHCAcceptedBytes_Object=MibTableColumn
wwpLeosTrafficProfileStdHCAcceptedBytes=_WwpLeosTrafficProfileStdHCAcceptedBytes_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,5),_WwpLeosTrafficProfileStdHCAcceptedBytes_Type())
wwpLeosTrafficProfileStdHCAcceptedBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdHCAcceptedBytes.setStatus(_A)
_WwpLeosTrafficProfileStdHCDroppedBytes_Type=Counter64
_WwpLeosTrafficProfileStdHCDroppedBytes_Object=MibTableColumn
wwpLeosTrafficProfileStdHCDroppedBytes=_WwpLeosTrafficProfileStdHCDroppedBytes_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,6),_WwpLeosTrafficProfileStdHCDroppedBytes_Type())
wwpLeosTrafficProfileStdHCDroppedBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdHCDroppedBytes.setStatus(_A)
_WwpLeosTrafficProfileStdHCAcceptedPackets_Type=Counter64
_WwpLeosTrafficProfileStdHCAcceptedPackets_Object=MibTableColumn
wwpLeosTrafficProfileStdHCAcceptedPackets=_WwpLeosTrafficProfileStdHCAcceptedPackets_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,7),_WwpLeosTrafficProfileStdHCAcceptedPackets_Type())
wwpLeosTrafficProfileStdHCAcceptedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdHCAcceptedPackets.setStatus(_A)
_WwpLeosTrafficProfileStdHCDroppedPackets_Type=Counter64
_WwpLeosTrafficProfileStdHCDroppedPackets_Object=MibTableColumn
wwpLeosTrafficProfileStdHCDroppedPackets=_WwpLeosTrafficProfileStdHCDroppedPackets_Object((1,3,6,1,4,1,6141,2,60,27,1,1,9,1,8),_WwpLeosTrafficProfileStdHCDroppedPackets_Type())
wwpLeosTrafficProfileStdHCDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdHCDroppedPackets.setStatus(_A)
_WwpLeosTrafficProfileCascadedGlobalTable_Object=MibTable
wwpLeosTrafficProfileCascadedGlobalTable=_WwpLeosTrafficProfileCascadedGlobalTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalTable.setStatus(_F)
_WwpLeosTrafficProfileCascadedGlobalEntry_Object=MibTableRow
wwpLeosTrafficProfileCascadedGlobalEntry=_WwpLeosTrafficProfileCascadedGlobalEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1))
wwpLeosTrafficProfileCascadedGlobalEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalEntry.setStatus(_F)
class _WwpLeosTrafficProfileCascadedGlobalDot1d_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_WwpLeosTrafficProfileCascadedGlobalDot1d_Type.__name__=_B
_WwpLeosTrafficProfileCascadedGlobalDot1d_Object=MibTableColumn
wwpLeosTrafficProfileCascadedGlobalDot1d=_WwpLeosTrafficProfileCascadedGlobalDot1d_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1,1),_WwpLeosTrafficProfileCascadedGlobalDot1d_Type())
wwpLeosTrafficProfileCascadedGlobalDot1d.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalDot1d.setStatus(_F)
class _WwpLeosTrafficProfileCascadedGlobalIpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_WwpLeosTrafficProfileCascadedGlobalIpPrec_Type.__name__=_B
_WwpLeosTrafficProfileCascadedGlobalIpPrec_Object=MibTableColumn
wwpLeosTrafficProfileCascadedGlobalIpPrec=_WwpLeosTrafficProfileCascadedGlobalIpPrec_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1,2),_WwpLeosTrafficProfileCascadedGlobalIpPrec_Type())
wwpLeosTrafficProfileCascadedGlobalIpPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalIpPrec.setStatus(_F)
class _WwpLeosTrafficProfileCascadedGlobalDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_WwpLeosTrafficProfileCascadedGlobalDscp_Type.__name__=_B
_WwpLeosTrafficProfileCascadedGlobalDscp_Object=MibTableColumn
wwpLeosTrafficProfileCascadedGlobalDscp=_WwpLeosTrafficProfileCascadedGlobalDscp_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1,3),_WwpLeosTrafficProfileCascadedGlobalDscp_Type())
wwpLeosTrafficProfileCascadedGlobalDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalDscp.setStatus(_F)
class _WwpLeosTrafficProfileCascadedGlobalName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeosTrafficProfileCascadedGlobalName_Type.__name__=_L
_WwpLeosTrafficProfileCascadedGlobalName_Object=MibTableColumn
wwpLeosTrafficProfileCascadedGlobalName=_WwpLeosTrafficProfileCascadedGlobalName_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1,4),_WwpLeosTrafficProfileCascadedGlobalName_Type())
wwpLeosTrafficProfileCascadedGlobalName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalName.setStatus(_F)
_WwpLeosTrafficProfileCascadedGlobalStatus_Type=RowStatus
_WwpLeosTrafficProfileCascadedGlobalStatus_Object=MibTableColumn
wwpLeosTrafficProfileCascadedGlobalStatus=_WwpLeosTrafficProfileCascadedGlobalStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,10,1,5),_WwpLeosTrafficProfileCascadedGlobalStatus_Type())
wwpLeosTrafficProfileCascadedGlobalStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedGlobalStatus.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalStatsTable_Object=MibTable
wwpLeosTrafficProfileCascadedTotalStatsTable=_WwpLeosTrafficProfileCascadedTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalStatsTable.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalStatsEntry_Object=MibTableRow
wwpLeosTrafficProfileCascadedTotalStatsEntry=_WwpLeosTrafficProfileCascadedTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1))
wwpLeosTrafficProfileCascadedTotalStatsEntry.setIndexNames((0,_E,_H),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalStatsEntry.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi=_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,1),_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Type())
wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo=_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,2),_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Type())
wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalDroppedBytesHi=_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,3),_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Type())
wwpLeosTrafficProfileCascadedTotalDroppedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalDroppedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalDroppedBytesLo=_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,4),_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Type())
wwpLeosTrafficProfileCascadedTotalDroppedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalDroppedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi=_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,5),_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Type())
wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi.setStatus(_F)
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Type=Counter32
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo=_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,11,1,6),_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Type())
wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo.setStatus(_F)
_WwpLeosTrafficProfileStdTotalStatsTable_Object=MibTable
wwpLeosTrafficProfileStdTotalStatsTable=_WwpLeosTrafficProfileStdTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalStatsTable.setStatus(_A)
_WwpLeosTrafficProfileStdTotalStatsEntry_Object=MibTableRow
wwpLeosTrafficProfileStdTotalStatsEntry=_WwpLeosTrafficProfileStdTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12,1))
wwpLeosTrafficProfileStdTotalStatsEntry.setIndexNames((0,_E,_H),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalStatsEntry.setStatus(_A)
_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Type=Counter32
_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileStdTotalAcceptedBytesHi=_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12,1,1),_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Type())
wwpLeosTrafficProfileStdTotalAcceptedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalAcceptedBytesHi.setStatus(_A)
_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Type=Counter32
_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileStdTotalAcceptedBytesLo=_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12,1,2),_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Type())
wwpLeosTrafficProfileStdTotalAcceptedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalAcceptedBytesLo.setStatus(_A)
_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Type=Counter32
_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Object=MibTableColumn
wwpLeosTrafficProfileStdTotalDroppedBytesHi=_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12,1,3),_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Type())
wwpLeosTrafficProfileStdTotalDroppedBytesHi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalDroppedBytesHi.setStatus(_A)
_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Type=Counter32
_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Object=MibTableColumn
wwpLeosTrafficProfileStdTotalDroppedBytesLo=_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Object((1,3,6,1,4,1,6141,2,60,27,1,1,12,1,4),_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Type())
wwpLeosTrafficProfileStdTotalDroppedBytesLo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdTotalDroppedBytesLo.setStatus(_A)
_WwpLeosTrafficProfileStdVlanTable_Object=MibTable
wwpLeosTrafficProfileStdVlanTable=_WwpLeosTrafficProfileStdVlanTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,14))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanTable.setStatus(_A)
_WwpLeosTrafficProfileStdVlanEntry_Object=MibTableRow
wwpLeosTrafficProfileStdVlanEntry=_WwpLeosTrafficProfileStdVlanEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,14,1))
wwpLeosTrafficProfileStdVlanEntry.setIndexNames((0,_E,_H),(0,_E,_b))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosTrafficProfileStdVlanIndex_Type.__name__=_B
_WwpLeosTrafficProfileStdVlanIndex_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanIndex=_WwpLeosTrafficProfileStdVlanIndex_Object((1,3,6,1,4,1,6141,2,60,27,1,1,14,1,1),_WwpLeosTrafficProfileStdVlanIndex_Type())
wwpLeosTrafficProfileStdVlanIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanIndex.setStatus(_A)
class _WwpLeosTrafficProfileStdVlanToProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosTrafficProfileStdVlanToProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdVlanToProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanToProfile=_WwpLeosTrafficProfileStdVlanToProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,14,1,2),_WwpLeosTrafficProfileStdVlanToProfile_Type())
wwpLeosTrafficProfileStdVlanToProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanToProfile.setStatus(_A)
_WwpLeosTrafficProfileStdVlanStatus_Type=RowStatus
_WwpLeosTrafficProfileStdVlanStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanStatus=_WwpLeosTrafficProfileStdVlanStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,14,1,3),_WwpLeosTrafficProfileStdVlanStatus_Type())
wwpLeosTrafficProfileStdVlanStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanStatus.setStatus(_A)
_WwpLeosTrafficProfileStdDscpTable_Object=MibTable
wwpLeosTrafficProfileStdDscpTable=_WwpLeosTrafficProfileStdDscpTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,15))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscpTable.setStatus(_A)
_WwpLeosTrafficProfileStdDscpEntry_Object=MibTableRow
wwpLeosTrafficProfileStdDscpEntry=_WwpLeosTrafficProfileStdDscpEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,15,1))
wwpLeosTrafficProfileStdDscpEntry.setIndexNames((0,_E,_H),(0,_E,_W))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscpEntry.setStatus(_A)
class _WwpLeosTrafficProfileStdDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTrafficProfileStdDscp_Type.__name__=_B
_WwpLeosTrafficProfileStdDscp_Object=MibTableColumn
wwpLeosTrafficProfileStdDscp=_WwpLeosTrafficProfileStdDscp_Object((1,3,6,1,4,1,6141,2,60,27,1,1,15,1,1),_WwpLeosTrafficProfileStdDscp_Type())
wwpLeosTrafficProfileStdDscp.setMaxAccess(_V)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscp.setStatus(_A)
class _WwpLeosTrafficProfileStdDscpToProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpLeosTrafficProfileStdDscpToProfile_Type.__name__=_B
_WwpLeosTrafficProfileStdDscpToProfile_Object=MibTableColumn
wwpLeosTrafficProfileStdDscpToProfile=_WwpLeosTrafficProfileStdDscpToProfile_Object((1,3,6,1,4,1,6141,2,60,27,1,1,15,1,2),_WwpLeosTrafficProfileStdDscpToProfile_Type())
wwpLeosTrafficProfileStdDscpToProfile.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscpToProfile.setStatus(_A)
_WwpLeosTrafficProfileStdDscpStatus_Type=RowStatus
_WwpLeosTrafficProfileStdDscpStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdDscpStatus=_WwpLeosTrafficProfileStdDscpStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,15,1,3),_WwpLeosTrafficProfileStdDscpStatus_Type())
wwpLeosTrafficProfileStdDscpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdDscpStatus.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolTable_Object=MibTable
wwpLeosTrafficProfileMeterPoolTable=_WwpLeosTrafficProfileMeterPoolTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16))
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolTable.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolEntry_Object=MibTableRow
wwpLeosTrafficProfileMeterPoolEntry=_WwpLeosTrafficProfileMeterPoolEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1))
wwpLeosTrafficProfileMeterPoolEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolEntry.setStatus(_A)
class _WwpLeosTrafficProfileMeterPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WwpLeosTrafficProfileMeterPoolIndex_Type.__name__=_B
_WwpLeosTrafficProfileMeterPoolIndex_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolIndex=_WwpLeosTrafficProfileMeterPoolIndex_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,1),_WwpLeosTrafficProfileMeterPoolIndex_Type())
wwpLeosTrafficProfileMeterPoolIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolIndex.setStatus(_A)
class _WwpLeosTrafficProfileMeterPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeosTrafficProfileMeterPoolName_Type.__name__=_L
_WwpLeosTrafficProfileMeterPoolName_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolName=_WwpLeosTrafficProfileMeterPoolName_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,2),_WwpLeosTrafficProfileMeterPoolName_Type())
wwpLeosTrafficProfileMeterPoolName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolName.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolNumOfMeters_Type=Integer32
_WwpLeosTrafficProfileMeterPoolNumOfMeters_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfMeters=_WwpLeosTrafficProfileMeterPoolNumOfMeters_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,3),_WwpLeosTrafficProfileMeterPoolNumOfMeters_Type())
wwpLeosTrafficProfileMeterPoolNumOfMeters.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolNumOfMeters.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolMetersUsed_Type=Integer32
_WwpLeosTrafficProfileMeterPoolMetersUsed_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolMetersUsed=_WwpLeosTrafficProfileMeterPoolMetersUsed_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,4),_WwpLeosTrafficProfileMeterPoolMetersUsed_Type())
wwpLeosTrafficProfileMeterPoolMetersUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolMetersUsed.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolNumOfStats_Type=Integer32
_WwpLeosTrafficProfileMeterPoolNumOfStats_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfStats=_WwpLeosTrafficProfileMeterPoolNumOfStats_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,5),_WwpLeosTrafficProfileMeterPoolNumOfStats_Type())
wwpLeosTrafficProfileMeterPoolNumOfStats.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolNumOfStats.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolStatsUsed_Type=Integer32
_WwpLeosTrafficProfileMeterPoolStatsUsed_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolStatsUsed=_WwpLeosTrafficProfileMeterPoolStatsUsed_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,6),_WwpLeosTrafficProfileMeterPoolStatsUsed_Type())
wwpLeosTrafficProfileMeterPoolStatsUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolStatsUsed.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Type=Integer32
_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfClassifiers=_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,7),_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Type())
wwpLeosTrafficProfileMeterPoolNumOfClassifiers.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolNumOfClassifiers.setStatus(_A)
_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Type=Integer32
_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Object=MibTableColumn
wwpLeosTrafficProfileMeterPoolClassifiersUsed=_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Object((1,3,6,1,4,1,6141,2,60,27,1,1,16,1,8),_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Type())
wwpLeosTrafficProfileMeterPoolClassifiersUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTrafficProfileMeterPoolClassifiersUsed.setStatus(_A)
_WwpLeosTrafficProfileTosStampTable_Object=MibTable
wwpLeosTrafficProfileTosStampTable=_WwpLeosTrafficProfileTosStampTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,20))
if mibBuilder.loadTexts:wwpLeosTrafficProfileTosStampTable.setStatus(_A)
_WwpLeosTrafficProfileTosStampEntry_Object=MibTableRow
wwpLeosTrafficProfileTosStampEntry=_WwpLeosTrafficProfileTosStampEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,20,1))
wwpLeosTrafficProfileTosStampEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosTrafficProfileTosStampEntry.setStatus(_A)
class _WwpLeosTrafficProfileTosStampState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileTosStampState_Type.__name__=_B
_WwpLeosTrafficProfileTosStampState_Object=MibTableColumn
wwpLeosTrafficProfileTosStampState=_WwpLeosTrafficProfileTosStampState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,20,1,1),_WwpLeosTrafficProfileTosStampState_Type())
wwpLeosTrafficProfileTosStampState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileTosStampState.setStatus(_A)
class _WwpLeosTrafficProfileTosStampValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTrafficProfileTosStampValue_Type.__name__=_B
_WwpLeosTrafficProfileTosStampValue_Object=MibTableColumn
wwpLeosTrafficProfileTosStampValue=_WwpLeosTrafficProfileTosStampValue_Object((1,3,6,1,4,1,6141,2,60,27,1,1,20,1,2),_WwpLeosTrafficProfileTosStampValue_Type())
wwpLeosTrafficProfileTosStampValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileTosStampValue.setStatus(_A)
_WwpLeosTrafficProfileIpDscpTable_Object=MibTable
wwpLeosTrafficProfileIpDscpTable=_WwpLeosTrafficProfileIpDscpTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21))
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpDscpTable.setStatus(_A)
_WwpLeosTrafficProfileIpDscpEntry_Object=MibTableRow
wwpLeosTrafficProfileIpDscpEntry=_WwpLeosTrafficProfileIpDscpEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1))
wwpLeosTrafficProfileIpDscpEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpDscpEntry.setStatus(_A)
class _WwpLeosTrafficProfileIpp0Cs0State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp0Cs0State_Type.__name__=_B
_WwpLeosTrafficProfileIpp0Cs0State_Object=MibTableColumn
wwpLeosTrafficProfileIpp0Cs0State=_WwpLeosTrafficProfileIpp0Cs0State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,1),_WwpLeosTrafficProfileIpp0Cs0State_Type())
wwpLeosTrafficProfileIpp0Cs0State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp0Cs0State.setStatus(_A)
class _WwpLeosTrafficProfileIpp1Cs1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp1Cs1State_Type.__name__=_B
_WwpLeosTrafficProfileIpp1Cs1State_Object=MibTableColumn
wwpLeosTrafficProfileIpp1Cs1State=_WwpLeosTrafficProfileIpp1Cs1State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,2),_WwpLeosTrafficProfileIpp1Cs1State_Type())
wwpLeosTrafficProfileIpp1Cs1State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp1Cs1State.setStatus(_A)
class _WwpLeosTrafficProfileIpp2Cs2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp2Cs2State_Type.__name__=_B
_WwpLeosTrafficProfileIpp2Cs2State_Object=MibTableColumn
wwpLeosTrafficProfileIpp2Cs2State=_WwpLeosTrafficProfileIpp2Cs2State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,3),_WwpLeosTrafficProfileIpp2Cs2State_Type())
wwpLeosTrafficProfileIpp2Cs2State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp2Cs2State.setStatus(_A)
class _WwpLeosTrafficProfileIpp3Cs3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp3Cs3State_Type.__name__=_B
_WwpLeosTrafficProfileIpp3Cs3State_Object=MibTableColumn
wwpLeosTrafficProfileIpp3Cs3State=_WwpLeosTrafficProfileIpp3Cs3State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,4),_WwpLeosTrafficProfileIpp3Cs3State_Type())
wwpLeosTrafficProfileIpp3Cs3State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp3Cs3State.setStatus(_A)
class _WwpLeosTrafficProfileIpp4Cs4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp4Cs4State_Type.__name__=_B
_WwpLeosTrafficProfileIpp4Cs4State_Object=MibTableColumn
wwpLeosTrafficProfileIpp4Cs4State=_WwpLeosTrafficProfileIpp4Cs4State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,5),_WwpLeosTrafficProfileIpp4Cs4State_Type())
wwpLeosTrafficProfileIpp4Cs4State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp4Cs4State.setStatus(_A)
class _WwpLeosTrafficProfileIpp5Cs5State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp5Cs5State_Type.__name__=_B
_WwpLeosTrafficProfileIpp5Cs5State_Object=MibTableColumn
wwpLeosTrafficProfileIpp5Cs5State=_WwpLeosTrafficProfileIpp5Cs5State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,6),_WwpLeosTrafficProfileIpp5Cs5State_Type())
wwpLeosTrafficProfileIpp5Cs5State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp5Cs5State.setStatus(_A)
class _WwpLeosTrafficProfileIpp6Cs6State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp6Cs6State_Type.__name__=_B
_WwpLeosTrafficProfileIpp6Cs6State_Object=MibTableColumn
wwpLeosTrafficProfileIpp6Cs6State=_WwpLeosTrafficProfileIpp6Cs6State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,7),_WwpLeosTrafficProfileIpp6Cs6State_Type())
wwpLeosTrafficProfileIpp6Cs6State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp6Cs6State.setStatus(_A)
class _WwpLeosTrafficProfileIpp7Cs7State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileIpp7Cs7State_Type.__name__=_B
_WwpLeosTrafficProfileIpp7Cs7State_Object=MibTableColumn
wwpLeosTrafficProfileIpp7Cs7State=_WwpLeosTrafficProfileIpp7Cs7State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,8),_WwpLeosTrafficProfileIpp7Cs7State_Type())
wwpLeosTrafficProfileIpp7Cs7State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileIpp7Cs7State.setStatus(_A)
class _WwpLeosTrafficProfileAf1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileAf1State_Type.__name__=_B
_WwpLeosTrafficProfileAf1State_Object=MibTableColumn
wwpLeosTrafficProfileAf1State=_WwpLeosTrafficProfileAf1State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,9),_WwpLeosTrafficProfileAf1State_Type())
wwpLeosTrafficProfileAf1State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileAf1State.setStatus(_A)
class _WwpLeosTrafficProfileAf2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileAf2State_Type.__name__=_B
_WwpLeosTrafficProfileAf2State_Object=MibTableColumn
wwpLeosTrafficProfileAf2State=_WwpLeosTrafficProfileAf2State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,10),_WwpLeosTrafficProfileAf2State_Type())
wwpLeosTrafficProfileAf2State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileAf2State.setStatus(_A)
class _WwpLeosTrafficProfileAf3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileAf3State_Type.__name__=_B
_WwpLeosTrafficProfileAf3State_Object=MibTableColumn
wwpLeosTrafficProfileAf3State=_WwpLeosTrafficProfileAf3State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,11),_WwpLeosTrafficProfileAf3State_Type())
wwpLeosTrafficProfileAf3State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileAf3State.setStatus(_A)
class _WwpLeosTrafficProfileAf4State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileAf4State_Type.__name__=_B
_WwpLeosTrafficProfileAf4State_Object=MibTableColumn
wwpLeosTrafficProfileAf4State=_WwpLeosTrafficProfileAf4State_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,12),_WwpLeosTrafficProfileAf4State_Type())
wwpLeosTrafficProfileAf4State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileAf4State.setStatus(_A)
class _WwpLeosTrafficProfileEfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosTrafficProfileEfState_Type.__name__=_B
_WwpLeosTrafficProfileEfState_Object=MibTableColumn
wwpLeosTrafficProfileEfState=_WwpLeosTrafficProfileEfState_Object((1,3,6,1,4,1,6141,2,60,27,1,1,21,1,13),_WwpLeosTrafficProfileEfState_Type())
wwpLeosTrafficProfileEfState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosTrafficProfileEfState.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDot1dTable_Object=MibTable
wwpLeosTrafficProfileStdVlanDot1dTable=_WwpLeosTrafficProfileStdVlanDot1dTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,40))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDot1dTable.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDot1dEntry_Object=MibTableRow
wwpLeosTrafficProfileStdVlanDot1dEntry=_WwpLeosTrafficProfileStdVlanDot1dEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,40,1))
wwpLeosTrafficProfileStdVlanDot1dEntry.setIndexNames((0,_E,_H),(0,_E,_T),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDot1dEntry.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDot1dStatus_Type=RowStatus
_WwpLeosTrafficProfileStdVlanDot1dStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanDot1dStatus=_WwpLeosTrafficProfileStdVlanDot1dStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,40,1,1),_WwpLeosTrafficProfileStdVlanDot1dStatus_Type())
wwpLeosTrafficProfileStdVlanDot1dStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDot1dStatus.setStatus(_A)
_WwpLeosTrafficProfileStdVlanIpPrecTable_Object=MibTable
wwpLeosTrafficProfileStdVlanIpPrecTable=_WwpLeosTrafficProfileStdVlanIpPrecTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,41))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanIpPrecTable.setStatus(_A)
_WwpLeosTrafficProfileStdVlanIpPrecEntry_Object=MibTableRow
wwpLeosTrafficProfileStdVlanIpPrecEntry=_WwpLeosTrafficProfileStdVlanIpPrecEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,41,1))
wwpLeosTrafficProfileStdVlanIpPrecEntry.setIndexNames((0,_E,_H),(0,_E,_U),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanIpPrecEntry.setStatus(_A)
_WwpLeosTrafficProfileStdVlanIpPrecStatus_Type=RowStatus
_WwpLeosTrafficProfileStdVlanIpPrecStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanIpPrecStatus=_WwpLeosTrafficProfileStdVlanIpPrecStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,41,1,1),_WwpLeosTrafficProfileStdVlanIpPrecStatus_Type())
wwpLeosTrafficProfileStdVlanIpPrecStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanIpPrecStatus.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDscpTable_Object=MibTable
wwpLeosTrafficProfileStdVlanDscpTable=_WwpLeosTrafficProfileStdVlanDscpTable_Object((1,3,6,1,4,1,6141,2,60,27,1,1,42))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDscpTable.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDscpEntry_Object=MibTableRow
wwpLeosTrafficProfileStdVlanDscpEntry=_WwpLeosTrafficProfileStdVlanDscpEntry_Object((1,3,6,1,4,1,6141,2,60,27,1,1,42,1))
wwpLeosTrafficProfileStdVlanDscpEntry.setIndexNames((0,_E,_H),(0,_E,_W),(0,_E,_K))
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDscpEntry.setStatus(_A)
_WwpLeosTrafficProfileStdVlanDscpStatus_Type=RowStatus
_WwpLeosTrafficProfileStdVlanDscpStatus_Object=MibTableColumn
wwpLeosTrafficProfileStdVlanDscpStatus=_WwpLeosTrafficProfileStdVlanDscpStatus_Object((1,3,6,1,4,1,6141,2,60,27,1,1,42,1,2),_WwpLeosTrafficProfileStdVlanDscpStatus_Type())
wwpLeosTrafficProfileStdVlanDscpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosTrafficProfileStdVlanDscpStatus.setStatus(_A)
_WwpLeosTrafficProfileNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileNotificationPrefix=_WwpLeosTrafficProfileNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,2))
_WwpLeosTrafficProfileNotifications_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileNotifications=_WwpLeosTrafficProfileNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,2,0))
_WwpLeosTrafficProfileMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileMIBConformance=_WwpLeosTrafficProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,3))
_WwpLeosTrafficProfileMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileMIBCompliances=_WwpLeosTrafficProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,3,1))
_WwpLeosTrafficProfileMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosTrafficProfileMIBGroups=_WwpLeosTrafficProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,27,3,2))
mibBuilder.exportSymbols(_E,**{'wwpLeosTrafficProfileMIB':wwpLeosTrafficProfileMIB,'wwpLeosTrafficProfileObjects':wwpLeosTrafficProfileObjects,'wwpLeosTrafficProfile':wwpLeosTrafficProfile,'wwpLeosTrafficProfileGlobalAttrs':wwpLeosTrafficProfileGlobalAttrs,'wwpLeosTrafficProfileGlobalState':wwpLeosTrafficProfileGlobalState,'wwpLeosTrafficProfileGlobalMeterProvisioningState':wwpLeosTrafficProfileGlobalMeterProvisioningState,'wwpLeosTrafficProfilePortTable':wwpLeosTrafficProfilePortTable,'wwpLeosTrafficProfilePortEntry':wwpLeosTrafficProfilePortEntry,_H:wwpLeosTrafficProfilePort,'wwpLeosTrafficProfileAdminState':wwpLeosTrafficProfileAdminState,'wwpLeosTrafficProfileOperState':wwpLeosTrafficProfileOperState,'wwpLeosTrafficProfileMode':wwpLeosTrafficProfileMode,'wwpLeosTrafficProfileNonConformCascadedProfile':wwpLeosTrafficProfileNonConformCascadedProfile,'wwpLeosTrafficProfileNonConformStdProfile':wwpLeosTrafficProfileNonConformStdProfile,'wwpLeosTrafficProfileArpCascadedProfile':wwpLeosTrafficProfileArpCascadedProfile,'wwpLeosTrafficProfileArpStdProfile':wwpLeosTrafficProfileArpStdProfile,'wwpLeosTrafficProfileMeterPool':wwpLeosTrafficProfileMeterPool,'wwpLeosTrafficProfileClassifierMode':wwpLeosTrafficProfileClassifierMode,'wwpLeosTrafficProfileCascadedTable':wwpLeosTrafficProfileCascadedTable,'wwpLeosTrafficProfileCascadedEntry':wwpLeosTrafficProfileCascadedEntry,_M:wwpLeosTrafficProfileCascadedIndx,'wwpLeosTrafficProfileCascadedCir':wwpLeosTrafficProfileCascadedCir,'wwpLeosTrafficProfileCascadedPir':wwpLeosTrafficProfileCascadedPir,'wwpLeosTrafficProfileCascadedStatus':wwpLeosTrafficProfileCascadedStatus,'wwpLeosTrafficProfileStdTable':wwpLeosTrafficProfileStdTable,'wwpLeosTrafficProfileStdEntry':wwpLeosTrafficProfileStdEntry,_K:wwpLeosTrafficProfileStdIndx,'wwpLeosTrafficProfileStdCir':wwpLeosTrafficProfileStdCir,'wwpLeosTrafficProfileStdPir':wwpLeosTrafficProfileStdPir,'wwpLeosTrafficProfileStdName':wwpLeosTrafficProfileStdName,'wwpLeosTrafficProfileStdStatus':wwpLeosTrafficProfileStdStatus,'wwpLeosTrafficProfileStdVlan':wwpLeosTrafficProfileStdVlan,'wwpLeosTrafficProfileStdCbs':wwpLeosTrafficProfileStdCbs,'wwpLeosTrafficProfileStdEbs':wwpLeosTrafficProfileStdEbs,'wwpLeosTrafficProfileStdDscpRemarkPolicy':wwpLeosTrafficProfileStdDscpRemarkPolicy,'wwpLeosTrafficProfileStdFixedDscp':wwpLeosTrafficProfileStdFixedDscp,'wwpLeosTrafficProfileStdUnsetVlan':wwpLeosTrafficProfileStdUnsetVlan,'wwpLeosTrafficProfileStdDefaultProfile':wwpLeosTrafficProfileStdDefaultProfile,'wwpLeosTrafficeProfileStdDrop':wwpLeosTrafficeProfileStdDrop,'wwpLeosTrafficProfileStdParentIndex':wwpLeosTrafficProfileStdParentIndex,'wwpLeosTrafficProfileStdChildMode':wwpLeosTrafficProfileStdChildMode,'wwpLeosTrafficProfileStdStatsMonitor':wwpLeosTrafficProfileStdStatsMonitor,'wwpLeosTrafficProfileStdUntaggedState':wwpLeosTrafficProfileStdUntaggedState,'wwpLeosTrafficProfileStdVs':wwpLeosTrafficProfileStdVs,'wwpLeosTrafficProfileStdRemarkColorPolicy':wwpLeosTrafficProfileStdRemarkColorPolicy,'wwpLeosTrafficProfileStdRemarkRcosPolicy':wwpLeosTrafficProfileStdRemarkRcosPolicy,'wwpLeosTrafficProfileStdYellowRemarkRcos':wwpLeosTrafficProfileStdYellowRemarkRcos,'wwpLeosTrafficProfileStdGreenRemarkRcos':wwpLeosTrafficProfileStdGreenRemarkRcos,'wwpLeosTrafficProfileStdIngressColorAware':wwpLeosTrafficProfileStdIngressColorAware,'wwpLeosTrafficProfileStdEir':wwpLeosTrafficProfileStdEir,'wwpLeosTrafficProfileStdDot1dTable':wwpLeosTrafficProfileStdDot1dTable,'wwpLeosTrafficProfileStdDot1dEntry':wwpLeosTrafficProfileStdDot1dEntry,_T:wwpLeosTrafficProfileStdDot1d,'wwpLeosTrafficProfileStdDot1dToProfile':wwpLeosTrafficProfileStdDot1dToProfile,'wwpLeosTrafficProfileStdDot1dStatus':wwpLeosTrafficProfileStdDot1dStatus,'wwpLeosTrafficProfileStdIpPrecTable':wwpLeosTrafficProfileStdIpPrecTable,'wwpLeosTrafficProfileStdIpPrecEntry':wwpLeosTrafficProfileStdIpPrecEntry,_U:wwpLeosTrafficProfileStdIpPrec,'wwpLeosTrafficProfileStdIpPrecToProfile':wwpLeosTrafficProfileStdIpPrecToProfile,'wwpLeosTrafficProfileStdIpPrecStatus':wwpLeosTrafficProfileStdIpPrecStatus,'wwpLeosTrafficProfileStdPhbTable':wwpLeosTrafficProfileStdPhbTable,'wwpLeosTrafficProfileStdPhbEntry':wwpLeosTrafficProfileStdPhbEntry,_a:wwpLeosTrafficProfileStdPhb,'wwpLeosTrafficProfileStdPhbToProfile':wwpLeosTrafficProfileStdPhbToProfile,'wwpLeosTrafficProfileStdPhbStatus':wwpLeosTrafficProfileStdPhbStatus,'wwpLeosTrafficProfileCascadedStatsTable':wwpLeosTrafficProfileCascadedStatsTable,'wwpLeosTrafficProfileCascadedStatsEntry':wwpLeosTrafficProfileCascadedStatsEntry,'wwpLeosTrafficProfileCascadedAcceptedBytesHi':wwpLeosTrafficProfileCascadedAcceptedBytesHi,'wwpLeosTrafficProfileCascadedAcceptedBytesLo':wwpLeosTrafficProfileCascadedAcceptedBytesLo,'wwpLeosTrafficProfileCascadedDroppedBytesHi':wwpLeosTrafficProfileCascadedDroppedBytesHi,'wwpLeosTrafficProfileCascadedDroppedBytesLo':wwpLeosTrafficProfileCascadedDroppedBytesLo,'wwpLeosTrafficProfileCascadedRemarkedBytesHi':wwpLeosTrafficProfileCascadedRemarkedBytesHi,'wwpLeosTrafficProfileCascadedRemarkedBytesLo':wwpLeosTrafficProfileCascadedRemarkedBytesLo,'wwpLeosTrafficProfileStdStatsTable':wwpLeosTrafficProfileStdStatsTable,'wwpLeosTrafficProfileStdStatsEntry':wwpLeosTrafficProfileStdStatsEntry,'wwpLeosTrafficProfileStdAcceptedBytesHi':wwpLeosTrafficProfileStdAcceptedBytesHi,'wwpLeosTrafficProfileStdAcceptedBytesLo':wwpLeosTrafficProfileStdAcceptedBytesLo,'wwpLeosTrafficProfileStdDroppedBytesHi':wwpLeosTrafficProfileStdDroppedBytesHi,'wwpLeosTrafficProfileStdDroppedBytesLo':wwpLeosTrafficProfileStdDroppedBytesLo,'wwpLeosTrafficProfileStdHCAcceptedBytes':wwpLeosTrafficProfileStdHCAcceptedBytes,'wwpLeosTrafficProfileStdHCDroppedBytes':wwpLeosTrafficProfileStdHCDroppedBytes,'wwpLeosTrafficProfileStdHCAcceptedPackets':wwpLeosTrafficProfileStdHCAcceptedPackets,'wwpLeosTrafficProfileStdHCDroppedPackets':wwpLeosTrafficProfileStdHCDroppedPackets,'wwpLeosTrafficProfileCascadedGlobalTable':wwpLeosTrafficProfileCascadedGlobalTable,'wwpLeosTrafficProfileCascadedGlobalEntry':wwpLeosTrafficProfileCascadedGlobalEntry,'wwpLeosTrafficProfileCascadedGlobalDot1d':wwpLeosTrafficProfileCascadedGlobalDot1d,'wwpLeosTrafficProfileCascadedGlobalIpPrec':wwpLeosTrafficProfileCascadedGlobalIpPrec,'wwpLeosTrafficProfileCascadedGlobalDscp':wwpLeosTrafficProfileCascadedGlobalDscp,'wwpLeosTrafficProfileCascadedGlobalName':wwpLeosTrafficProfileCascadedGlobalName,'wwpLeosTrafficProfileCascadedGlobalStatus':wwpLeosTrafficProfileCascadedGlobalStatus,'wwpLeosTrafficProfileCascadedTotalStatsTable':wwpLeosTrafficProfileCascadedTotalStatsTable,'wwpLeosTrafficProfileCascadedTotalStatsEntry':wwpLeosTrafficProfileCascadedTotalStatsEntry,'wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi':wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi,'wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo':wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo,'wwpLeosTrafficProfileCascadedTotalDroppedBytesHi':wwpLeosTrafficProfileCascadedTotalDroppedBytesHi,'wwpLeosTrafficProfileCascadedTotalDroppedBytesLo':wwpLeosTrafficProfileCascadedTotalDroppedBytesLo,'wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi':wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi,'wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo':wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo,'wwpLeosTrafficProfileStdTotalStatsTable':wwpLeosTrafficProfileStdTotalStatsTable,'wwpLeosTrafficProfileStdTotalStatsEntry':wwpLeosTrafficProfileStdTotalStatsEntry,'wwpLeosTrafficProfileStdTotalAcceptedBytesHi':wwpLeosTrafficProfileStdTotalAcceptedBytesHi,'wwpLeosTrafficProfileStdTotalAcceptedBytesLo':wwpLeosTrafficProfileStdTotalAcceptedBytesLo,'wwpLeosTrafficProfileStdTotalDroppedBytesHi':wwpLeosTrafficProfileStdTotalDroppedBytesHi,'wwpLeosTrafficProfileStdTotalDroppedBytesLo':wwpLeosTrafficProfileStdTotalDroppedBytesLo,'wwpLeosTrafficProfileStdVlanTable':wwpLeosTrafficProfileStdVlanTable,'wwpLeosTrafficProfileStdVlanEntry':wwpLeosTrafficProfileStdVlanEntry,_b:wwpLeosTrafficProfileStdVlanIndex,'wwpLeosTrafficProfileStdVlanToProfile':wwpLeosTrafficProfileStdVlanToProfile,'wwpLeosTrafficProfileStdVlanStatus':wwpLeosTrafficProfileStdVlanStatus,'wwpLeosTrafficProfileStdDscpTable':wwpLeosTrafficProfileStdDscpTable,'wwpLeosTrafficProfileStdDscpEntry':wwpLeosTrafficProfileStdDscpEntry,_W:wwpLeosTrafficProfileStdDscp,'wwpLeosTrafficProfileStdDscpToProfile':wwpLeosTrafficProfileStdDscpToProfile,'wwpLeosTrafficProfileStdDscpStatus':wwpLeosTrafficProfileStdDscpStatus,'wwpLeosTrafficProfileMeterPoolTable':wwpLeosTrafficProfileMeterPoolTable,'wwpLeosTrafficProfileMeterPoolEntry':wwpLeosTrafficProfileMeterPoolEntry,_c:wwpLeosTrafficProfileMeterPoolIndex,'wwpLeosTrafficProfileMeterPoolName':wwpLeosTrafficProfileMeterPoolName,'wwpLeosTrafficProfileMeterPoolNumOfMeters':wwpLeosTrafficProfileMeterPoolNumOfMeters,'wwpLeosTrafficProfileMeterPoolMetersUsed':wwpLeosTrafficProfileMeterPoolMetersUsed,'wwpLeosTrafficProfileMeterPoolNumOfStats':wwpLeosTrafficProfileMeterPoolNumOfStats,'wwpLeosTrafficProfileMeterPoolStatsUsed':wwpLeosTrafficProfileMeterPoolStatsUsed,'wwpLeosTrafficProfileMeterPoolNumOfClassifiers':wwpLeosTrafficProfileMeterPoolNumOfClassifiers,'wwpLeosTrafficProfileMeterPoolClassifiersUsed':wwpLeosTrafficProfileMeterPoolClassifiersUsed,'wwpLeosTrafficProfileTosStampTable':wwpLeosTrafficProfileTosStampTable,'wwpLeosTrafficProfileTosStampEntry':wwpLeosTrafficProfileTosStampEntry,'wwpLeosTrafficProfileTosStampState':wwpLeosTrafficProfileTosStampState,'wwpLeosTrafficProfileTosStampValue':wwpLeosTrafficProfileTosStampValue,'wwpLeosTrafficProfileIpDscpTable':wwpLeosTrafficProfileIpDscpTable,'wwpLeosTrafficProfileIpDscpEntry':wwpLeosTrafficProfileIpDscpEntry,'wwpLeosTrafficProfileIpp0Cs0State':wwpLeosTrafficProfileIpp0Cs0State,'wwpLeosTrafficProfileIpp1Cs1State':wwpLeosTrafficProfileIpp1Cs1State,'wwpLeosTrafficProfileIpp2Cs2State':wwpLeosTrafficProfileIpp2Cs2State,'wwpLeosTrafficProfileIpp3Cs3State':wwpLeosTrafficProfileIpp3Cs3State,'wwpLeosTrafficProfileIpp4Cs4State':wwpLeosTrafficProfileIpp4Cs4State,'wwpLeosTrafficProfileIpp5Cs5State':wwpLeosTrafficProfileIpp5Cs5State,'wwpLeosTrafficProfileIpp6Cs6State':wwpLeosTrafficProfileIpp6Cs6State,'wwpLeosTrafficProfileIpp7Cs7State':wwpLeosTrafficProfileIpp7Cs7State,'wwpLeosTrafficProfileAf1State':wwpLeosTrafficProfileAf1State,'wwpLeosTrafficProfileAf2State':wwpLeosTrafficProfileAf2State,'wwpLeosTrafficProfileAf3State':wwpLeosTrafficProfileAf3State,'wwpLeosTrafficProfileAf4State':wwpLeosTrafficProfileAf4State,'wwpLeosTrafficProfileEfState':wwpLeosTrafficProfileEfState,'wwpLeosTrafficProfileStdVlanDot1dTable':wwpLeosTrafficProfileStdVlanDot1dTable,'wwpLeosTrafficProfileStdVlanDot1dEntry':wwpLeosTrafficProfileStdVlanDot1dEntry,'wwpLeosTrafficProfileStdVlanDot1dStatus':wwpLeosTrafficProfileStdVlanDot1dStatus,'wwpLeosTrafficProfileStdVlanIpPrecTable':wwpLeosTrafficProfileStdVlanIpPrecTable,'wwpLeosTrafficProfileStdVlanIpPrecEntry':wwpLeosTrafficProfileStdVlanIpPrecEntry,'wwpLeosTrafficProfileStdVlanIpPrecStatus':wwpLeosTrafficProfileStdVlanIpPrecStatus,'wwpLeosTrafficProfileStdVlanDscpTable':wwpLeosTrafficProfileStdVlanDscpTable,'wwpLeosTrafficProfileStdVlanDscpEntry':wwpLeosTrafficProfileStdVlanDscpEntry,'wwpLeosTrafficProfileStdVlanDscpStatus':wwpLeosTrafficProfileStdVlanDscpStatus,'wwpLeosTrafficProfileNotificationPrefix':wwpLeosTrafficProfileNotificationPrefix,'wwpLeosTrafficProfileNotifications':wwpLeosTrafficProfileNotifications,'wwpLeosTrafficProfileMIBConformance':wwpLeosTrafficProfileMIBConformance,'wwpLeosTrafficProfileMIBCompliances':wwpLeosTrafficProfileMIBCompliances,'wwpLeosTrafficProfileMIBGroups':wwpLeosTrafficProfileMIBGroups})