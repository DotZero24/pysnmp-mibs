_AA='atmSoftPvcAddressMIBGroup'
_A9='atmSoftPvcVccMIBGroup'
_A8='atmSoftPvcBaseMIBGroup'
_A7='atmCurrentlyFailingSoftPVpcTimeStamp'
_A6='atmCurrentlyFailingSoftPVccTimeStamp'
_A5='atmInterfaceSoftPvcAddressRowStatus'
_A4='atmSoftPVpcRowStatus'
_A3='atmSoftPVpcRetryLimit'
_A2='atmSoftPVpcRetryFailures'
_A1='atmSoftPVpcRetryThreshold'
_A0='atmSoftPVpcRetryTimer'
_z='atmSoftPVpcRetryInterval'
_y='atmSoftPVpcRestart'
_x='atmSoftPVpcOperStatus'
_w='atmSoftPVpcLastReleaseDiagnostic'
_v='atmSoftPVpcLastReleaseCause'
_u='atmSoftPVpcTargetVpi'
_t='atmSoftPVpcTargetSelectType'
_s='atmSoftPVpcTargetAddress'
_r='atmSoftPVccRowStatus'
_q='atmSoftPVccRetryLimit'
_p='atmSoftPVccRetryFailures'
_o='atmSoftPVccRetryThreshold'
_n='atmSoftPVccRetryTimer'
_m='atmSoftPVccRetryInterval'
_l='atmSoftPVccRestart'
_k='atmSoftPVccOperStatus'
_j='atmSoftPVccLastReleaseDiagnostic'
_i='atmSoftPVccLastReleaseCause'
_h='atmSoftPVccTargetVci'
_g='atmSoftPVccTargetVpi'
_f='atmSoftPVccTargetSelectType'
_e='atmSoftPVccTargetAddress'
_d='atmSoftPvcNotificationInterval'
_c='atmSoftPvcCallFailuresTrapEnable'
_b='atmInterfaceSoftPvcAddress'
_a='restart'
_Z='lowerLayerDown'
_Y='noAddressSupplied'
_X='retriesExhausted'
_W='connected'
_V='establishmentInProgress'
_U='required'
_T='read-write'
_S='atmVplVpi'
_R='atmSoftPvcCurrentlyFailingSoftPVpcs'
_Q='atmSoftPvcCurrentlyFailingSoftPVccs'
_P='atmSoftPvcCallFailures'
_O='atmSoftPVpcLeafReference'
_N='not-accessible'
_M='atmSoftPVccLeafReference'
_L='atmVclVci'
_K='OctetString'
_J='atmVclVpi'
_I='seconds'
_H='ifIndex'
_G='IF-MIB'
_F='ATM-MIB'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='ATM-SOFT-PVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi,atmVplVpi=mibBuilder.importSymbols(_F,_L,_J,_S)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
atmSoftPvcMIB=ModuleIdentity((1,3,6,1,4,1,353,5,5,1))
if mibBuilder.loadTexts:atmSoftPvcMIB.setRevisions(('1997-03-01 00:00','1996-06-21 00:00'))
class AtmAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(20,20))
_AtmForum_ObjectIdentity=ObjectIdentity
atmForum=_AtmForum_ObjectIdentity((1,3,6,1,4,1,353))
_AtmForumNetworkManagement_ObjectIdentity=ObjectIdentity
atmForumNetworkManagement=_AtmForumNetworkManagement_ObjectIdentity((1,3,6,1,4,1,353,5))
_AtmfSoftPvc_ObjectIdentity=ObjectIdentity
atmfSoftPvc=_AtmfSoftPvc_ObjectIdentity((1,3,6,1,4,1,353,5,5))
_AtmSoftPvcMIBObjects_ObjectIdentity=ObjectIdentity
atmSoftPvcMIBObjects=_AtmSoftPvcMIBObjects_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,1))
_AtmSoftPvcBaseGroup_ObjectIdentity=ObjectIdentity
atmSoftPvcBaseGroup=_AtmSoftPvcBaseGroup_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,1,1))
_AtmSoftPvcCallFailuresTrapEnable_Type=TruthValue
_AtmSoftPvcCallFailuresTrapEnable_Object=MibScalar
atmSoftPvcCallFailuresTrapEnable=_AtmSoftPvcCallFailuresTrapEnable_Object((1,3,6,1,4,1,353,5,5,1,1,1,1),_AtmSoftPvcCallFailuresTrapEnable_Type())
atmSoftPvcCallFailuresTrapEnable.setMaxAccess(_T)
if mibBuilder.loadTexts:atmSoftPvcCallFailuresTrapEnable.setStatus(_A)
_AtmSoftPvcCallFailures_Type=Counter32
_AtmSoftPvcCallFailures_Object=MibScalar
atmSoftPvcCallFailures=_AtmSoftPvcCallFailures_Object((1,3,6,1,4,1,353,5,5,1,1,1,2),_AtmSoftPvcCallFailures_Type())
atmSoftPvcCallFailures.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPvcCallFailures.setStatus(_A)
_AtmSoftPvcCurrentlyFailingSoftPVccs_Type=Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVccs_Object=MibScalar
atmSoftPvcCurrentlyFailingSoftPVccs=_AtmSoftPvcCurrentlyFailingSoftPVccs_Object((1,3,6,1,4,1,353,5,5,1,1,1,3),_AtmSoftPvcCurrentlyFailingSoftPVccs_Type())
atmSoftPvcCurrentlyFailingSoftPVccs.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPvcCurrentlyFailingSoftPVccs.setStatus(_A)
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Type=Gauge32
_AtmSoftPvcCurrentlyFailingSoftPVpcs_Object=MibScalar
atmSoftPvcCurrentlyFailingSoftPVpcs=_AtmSoftPvcCurrentlyFailingSoftPVpcs_Object((1,3,6,1,4,1,353,5,5,1,1,1,4),_AtmSoftPvcCurrentlyFailingSoftPVpcs_Type())
atmSoftPvcCurrentlyFailingSoftPVpcs.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPvcCurrentlyFailingSoftPVpcs.setStatus(_A)
class _AtmSoftPvcNotificationInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AtmSoftPvcNotificationInterval_Type.__name__=_C
_AtmSoftPvcNotificationInterval_Object=MibScalar
atmSoftPvcNotificationInterval=_AtmSoftPvcNotificationInterval_Object((1,3,6,1,4,1,353,5,5,1,1,1,5),_AtmSoftPvcNotificationInterval_Type())
atmSoftPvcNotificationInterval.setMaxAccess(_T)
if mibBuilder.loadTexts:atmSoftPvcNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:atmSoftPvcNotificationInterval.setUnits(_I)
_AtmSoftPVccTable_Object=MibTable
atmSoftPVccTable=_AtmSoftPVccTable_Object((1,3,6,1,4,1,353,5,5,1,1,2))
if mibBuilder.loadTexts:atmSoftPVccTable.setStatus(_A)
_AtmSoftPVccEntry_Object=MibTableRow
atmSoftPVccEntry=_AtmSoftPVccEntry_Object((1,3,6,1,4,1,353,5,5,1,1,2,1))
atmSoftPVccEntry.setIndexNames((0,_G,_H),(0,_F,_J),(0,_F,_L),(0,_B,_M))
if mibBuilder.loadTexts:atmSoftPVccEntry.setStatus(_A)
class _AtmSoftPVccLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtmSoftPVccLeafReference_Type.__name__=_C
_AtmSoftPVccLeafReference_Object=MibTableColumn
atmSoftPVccLeafReference=_AtmSoftPVccLeafReference_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,1),_AtmSoftPVccLeafReference_Type())
atmSoftPVccLeafReference.setMaxAccess(_N)
if mibBuilder.loadTexts:atmSoftPVccLeafReference.setStatus(_A)
_AtmSoftPVccTargetAddress_Type=AtmAddr
_AtmSoftPVccTargetAddress_Object=MibTableColumn
atmSoftPVccTargetAddress=_AtmSoftPVccTargetAddress_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,2),_AtmSoftPVccTargetAddress_Type())
atmSoftPVccTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccTargetAddress.setStatus(_A)
class _AtmSoftPVccTargetSelectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('any',2)))
_AtmSoftPVccTargetSelectType_Type.__name__=_C
_AtmSoftPVccTargetSelectType_Object=MibTableColumn
atmSoftPVccTargetSelectType=_AtmSoftPVccTargetSelectType_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,3),_AtmSoftPVccTargetSelectType_Type())
atmSoftPVccTargetSelectType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccTargetSelectType.setStatus(_A)
class _AtmSoftPVccTargetVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmSoftPVccTargetVpi_Type.__name__=_C
_AtmSoftPVccTargetVpi_Object=MibTableColumn
atmSoftPVccTargetVpi=_AtmSoftPVccTargetVpi_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,4),_AtmSoftPVccTargetVpi_Type())
atmSoftPVccTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccTargetVpi.setStatus(_A)
class _AtmSoftPVccTargetVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmSoftPVccTargetVci_Type.__name__=_C
_AtmSoftPVccTargetVci_Object=MibTableColumn
atmSoftPVccTargetVci=_AtmSoftPVccTargetVci_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,5),_AtmSoftPVccTargetVci_Type())
atmSoftPVccTargetVci.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccTargetVci.setStatus(_A)
class _AtmSoftPVccLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_AtmSoftPVccLastReleaseCause_Type.__name__=_C
_AtmSoftPVccLastReleaseCause_Object=MibTableColumn
atmSoftPVccLastReleaseCause=_AtmSoftPVccLastReleaseCause_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,6),_AtmSoftPVccLastReleaseCause_Type())
atmSoftPVccLastReleaseCause.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVccLastReleaseCause.setStatus(_A)
class _AtmSoftPVccLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AtmSoftPVccLastReleaseDiagnostic_Type.__name__=_K
_AtmSoftPVccLastReleaseDiagnostic_Object=MibTableColumn
atmSoftPVccLastReleaseDiagnostic=_AtmSoftPVccLastReleaseDiagnostic_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,7),_AtmSoftPVccLastReleaseDiagnostic_Type())
atmSoftPVccLastReleaseDiagnostic.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVccLastReleaseDiagnostic.setStatus(_A)
class _AtmSoftPVccOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_AtmSoftPVccOperStatus_Type.__name__=_C
_AtmSoftPVccOperStatus_Object=MibTableColumn
atmSoftPVccOperStatus=_AtmSoftPVccOperStatus_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,8),_AtmSoftPVccOperStatus_Type())
atmSoftPVccOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVccOperStatus.setStatus(_A)
class _AtmSoftPVccRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('noop',2)))
_AtmSoftPVccRestart_Type.__name__=_C
_AtmSoftPVccRestart_Object=MibTableColumn
atmSoftPVccRestart=_AtmSoftPVccRestart_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,9),_AtmSoftPVccRestart_Type())
atmSoftPVccRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccRestart.setStatus(_A)
class _AtmSoftPVccRetryInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AtmSoftPVccRetryInterval_Type.__name__=_C
_AtmSoftPVccRetryInterval_Object=MibTableColumn
atmSoftPVccRetryInterval=_AtmSoftPVccRetryInterval_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,10),_AtmSoftPVccRetryInterval_Type())
atmSoftPVccRetryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:atmSoftPVccRetryInterval.setUnits(_I)
class _AtmSoftPVccRetryTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_AtmSoftPVccRetryTimer_Type.__name__=_C
_AtmSoftPVccRetryTimer_Object=MibTableColumn
atmSoftPVccRetryTimer=_AtmSoftPVccRetryTimer_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,11),_AtmSoftPVccRetryTimer_Type())
atmSoftPVccRetryTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVccRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:atmSoftPVccRetryTimer.setUnits(_I)
class _AtmSoftPVccRetryThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmSoftPVccRetryThreshold_Type.__name__=_C
_AtmSoftPVccRetryThreshold_Object=MibTableColumn
atmSoftPVccRetryThreshold=_AtmSoftPVccRetryThreshold_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,12),_AtmSoftPVccRetryThreshold_Type())
atmSoftPVccRetryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccRetryThreshold.setStatus(_A)
_AtmSoftPVccRetryFailures_Type=Gauge32
_AtmSoftPVccRetryFailures_Object=MibTableColumn
atmSoftPVccRetryFailures=_AtmSoftPVccRetryFailures_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,13),_AtmSoftPVccRetryFailures_Type())
atmSoftPVccRetryFailures.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVccRetryFailures.setStatus(_A)
class _AtmSoftPVccRetryLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmSoftPVccRetryLimit_Type.__name__=_C
_AtmSoftPVccRetryLimit_Object=MibTableColumn
atmSoftPVccRetryLimit=_AtmSoftPVccRetryLimit_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,14),_AtmSoftPVccRetryLimit_Type())
atmSoftPVccRetryLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccRetryLimit.setStatus(_A)
_AtmSoftPVccRowStatus_Type=RowStatus
_AtmSoftPVccRowStatus_Object=MibTableColumn
atmSoftPVccRowStatus=_AtmSoftPVccRowStatus_Object((1,3,6,1,4,1,353,5,5,1,1,2,1,15),_AtmSoftPVccRowStatus_Type())
atmSoftPVccRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVccRowStatus.setStatus(_A)
_AtmSoftPVpcTable_Object=MibTable
atmSoftPVpcTable=_AtmSoftPVpcTable_Object((1,3,6,1,4,1,353,5,5,1,1,3))
if mibBuilder.loadTexts:atmSoftPVpcTable.setStatus(_A)
_AtmSoftPVpcEntry_Object=MibTableRow
atmSoftPVpcEntry=_AtmSoftPVpcEntry_Object((1,3,6,1,4,1,353,5,5,1,1,3,1))
atmSoftPVpcEntry.setIndexNames((0,_G,_H),(0,_F,_S),(0,_B,_O))
if mibBuilder.loadTexts:atmSoftPVpcEntry.setStatus(_A)
class _AtmSoftPVpcLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63535))
_AtmSoftPVpcLeafReference_Type.__name__=_C
_AtmSoftPVpcLeafReference_Object=MibTableColumn
atmSoftPVpcLeafReference=_AtmSoftPVpcLeafReference_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,1),_AtmSoftPVpcLeafReference_Type())
atmSoftPVpcLeafReference.setMaxAccess(_N)
if mibBuilder.loadTexts:atmSoftPVpcLeafReference.setStatus(_A)
_AtmSoftPVpcTargetAddress_Type=AtmAddr
_AtmSoftPVpcTargetAddress_Object=MibTableColumn
atmSoftPVpcTargetAddress=_AtmSoftPVpcTargetAddress_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,2),_AtmSoftPVpcTargetAddress_Type())
atmSoftPVpcTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcTargetAddress.setStatus(_A)
class _AtmSoftPVpcTargetSelectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('any',2)))
_AtmSoftPVpcTargetSelectType_Type.__name__=_C
_AtmSoftPVpcTargetSelectType_Object=MibTableColumn
atmSoftPVpcTargetSelectType=_AtmSoftPVpcTargetSelectType_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,3),_AtmSoftPVpcTargetSelectType_Type())
atmSoftPVpcTargetSelectType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcTargetSelectType.setStatus(_A)
class _AtmSoftPVpcTargetVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmSoftPVpcTargetVpi_Type.__name__=_C
_AtmSoftPVpcTargetVpi_Object=MibTableColumn
atmSoftPVpcTargetVpi=_AtmSoftPVpcTargetVpi_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,4),_AtmSoftPVpcTargetVpi_Type())
atmSoftPVpcTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcTargetVpi.setStatus(_A)
class _AtmSoftPVpcLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_AtmSoftPVpcLastReleaseCause_Type.__name__=_C
_AtmSoftPVpcLastReleaseCause_Object=MibTableColumn
atmSoftPVpcLastReleaseCause=_AtmSoftPVpcLastReleaseCause_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,5),_AtmSoftPVpcLastReleaseCause_Type())
atmSoftPVpcLastReleaseCause.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVpcLastReleaseCause.setStatus(_A)
class _AtmSoftPVpcLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AtmSoftPVpcLastReleaseDiagnostic_Type.__name__=_K
_AtmSoftPVpcLastReleaseDiagnostic_Object=MibTableColumn
atmSoftPVpcLastReleaseDiagnostic=_AtmSoftPVpcLastReleaseDiagnostic_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,6),_AtmSoftPVpcLastReleaseDiagnostic_Type())
atmSoftPVpcLastReleaseDiagnostic.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVpcLastReleaseDiagnostic.setStatus(_A)
class _AtmSoftPVpcOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6)))
_AtmSoftPVpcOperStatus_Type.__name__=_C
_AtmSoftPVpcOperStatus_Object=MibTableColumn
atmSoftPVpcOperStatus=_AtmSoftPVpcOperStatus_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,7),_AtmSoftPVpcOperStatus_Type())
atmSoftPVpcOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVpcOperStatus.setStatus(_A)
class _AtmSoftPVpcRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('noop',2)))
_AtmSoftPVpcRestart_Type.__name__=_C
_AtmSoftPVpcRestart_Object=MibTableColumn
atmSoftPVpcRestart=_AtmSoftPVpcRestart_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,8),_AtmSoftPVpcRestart_Type())
atmSoftPVpcRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcRestart.setStatus(_A)
class _AtmSoftPVpcRetryInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AtmSoftPVpcRetryInterval_Type.__name__=_C
_AtmSoftPVpcRetryInterval_Object=MibTableColumn
atmSoftPVpcRetryInterval=_AtmSoftPVpcRetryInterval_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,9),_AtmSoftPVpcRetryInterval_Type())
atmSoftPVpcRetryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:atmSoftPVpcRetryInterval.setUnits(_I)
class _AtmSoftPVpcRetryTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_AtmSoftPVpcRetryTimer_Type.__name__=_C
_AtmSoftPVpcRetryTimer_Object=MibTableColumn
atmSoftPVpcRetryTimer=_AtmSoftPVpcRetryTimer_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,10),_AtmSoftPVpcRetryTimer_Type())
atmSoftPVpcRetryTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVpcRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:atmSoftPVpcRetryTimer.setUnits(_I)
class _AtmSoftPVpcRetryThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmSoftPVpcRetryThreshold_Type.__name__=_C
_AtmSoftPVpcRetryThreshold_Object=MibTableColumn
atmSoftPVpcRetryThreshold=_AtmSoftPVpcRetryThreshold_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,11),_AtmSoftPVpcRetryThreshold_Type())
atmSoftPVpcRetryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcRetryThreshold.setStatus(_A)
_AtmSoftPVpcRetryFailures_Type=Gauge32
_AtmSoftPVpcRetryFailures_Object=MibTableColumn
atmSoftPVpcRetryFailures=_AtmSoftPVpcRetryFailures_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,12),_AtmSoftPVpcRetryFailures_Type())
atmSoftPVpcRetryFailures.setMaxAccess(_E)
if mibBuilder.loadTexts:atmSoftPVpcRetryFailures.setStatus(_A)
class _AtmSoftPVpcRetryLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmSoftPVpcRetryLimit_Type.__name__=_C
_AtmSoftPVpcRetryLimit_Object=MibTableColumn
atmSoftPVpcRetryLimit=_AtmSoftPVpcRetryLimit_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,13),_AtmSoftPVpcRetryLimit_Type())
atmSoftPVpcRetryLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcRetryLimit.setStatus(_A)
_AtmSoftPVpcRowStatus_Type=RowStatus
_AtmSoftPVpcRowStatus_Object=MibTableColumn
atmSoftPVpcRowStatus=_AtmSoftPVpcRowStatus_Object((1,3,6,1,4,1,353,5,5,1,1,3,1,14),_AtmSoftPVpcRowStatus_Type())
atmSoftPVpcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmSoftPVpcRowStatus.setStatus(_A)
_AtmInterfaceSoftPvcAddressTable_Object=MibTable
atmInterfaceSoftPvcAddressTable=_AtmInterfaceSoftPvcAddressTable_Object((1,3,6,1,4,1,353,5,5,1,1,4))
if mibBuilder.loadTexts:atmInterfaceSoftPvcAddressTable.setStatus(_A)
_AtmInterfaceSoftPvcAddressEntry_Object=MibTableRow
atmInterfaceSoftPvcAddressEntry=_AtmInterfaceSoftPvcAddressEntry_Object((1,3,6,1,4,1,353,5,5,1,1,4,1))
atmInterfaceSoftPvcAddressEntry.setIndexNames((0,_G,_H),(0,_B,_b))
if mibBuilder.loadTexts:atmInterfaceSoftPvcAddressEntry.setStatus(_A)
_AtmInterfaceSoftPvcAddress_Type=AtmAddr
_AtmInterfaceSoftPvcAddress_Object=MibTableColumn
atmInterfaceSoftPvcAddress=_AtmInterfaceSoftPvcAddress_Object((1,3,6,1,4,1,353,5,5,1,1,4,1,1),_AtmInterfaceSoftPvcAddress_Type())
atmInterfaceSoftPvcAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:atmInterfaceSoftPvcAddress.setStatus(_A)
_AtmInterfaceSoftPvcAddressRowStatus_Type=RowStatus
_AtmInterfaceSoftPvcAddressRowStatus_Object=MibTableColumn
atmInterfaceSoftPvcAddressRowStatus=_AtmInterfaceSoftPvcAddressRowStatus_Object((1,3,6,1,4,1,353,5,5,1,1,4,1,2),_AtmInterfaceSoftPvcAddressRowStatus_Type())
atmInterfaceSoftPvcAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmInterfaceSoftPvcAddressRowStatus.setStatus(_A)
_AtmCurrentlyFailingSoftPVccTable_Object=MibTable
atmCurrentlyFailingSoftPVccTable=_AtmCurrentlyFailingSoftPVccTable_Object((1,3,6,1,4,1,353,5,5,1,1,5))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVccTable.setStatus(_A)
_AtmCurrentlyFailingSoftPVccEntry_Object=MibTableRow
atmCurrentlyFailingSoftPVccEntry=_AtmCurrentlyFailingSoftPVccEntry_Object((1,3,6,1,4,1,353,5,5,1,1,5,1))
atmCurrentlyFailingSoftPVccEntry.setIndexNames((0,_G,_H),(0,_F,_J),(0,_F,_L),(0,_B,_M))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVccEntry.setStatus(_A)
_AtmCurrentlyFailingSoftPVccTimeStamp_Type=TimeStamp
_AtmCurrentlyFailingSoftPVccTimeStamp_Object=MibTableColumn
atmCurrentlyFailingSoftPVccTimeStamp=_AtmCurrentlyFailingSoftPVccTimeStamp_Object((1,3,6,1,4,1,353,5,5,1,1,5,1,1),_AtmCurrentlyFailingSoftPVccTimeStamp_Type())
atmCurrentlyFailingSoftPVccTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVccTimeStamp.setStatus(_A)
_AtmCurrentlyFailingSoftPVpcTable_Object=MibTable
atmCurrentlyFailingSoftPVpcTable=_AtmCurrentlyFailingSoftPVpcTable_Object((1,3,6,1,4,1,353,5,5,1,1,6))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVpcTable.setStatus(_A)
_AtmCurrentlyFailingSoftPVpcEntry_Object=MibTableRow
atmCurrentlyFailingSoftPVpcEntry=_AtmCurrentlyFailingSoftPVpcEntry_Object((1,3,6,1,4,1,353,5,5,1,1,6,1))
atmCurrentlyFailingSoftPVpcEntry.setIndexNames((0,_G,_H),(0,_F,_J),(0,_B,_O))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVpcEntry.setStatus(_A)
_AtmCurrentlyFailingSoftPVpcTimeStamp_Type=TimeStamp
_AtmCurrentlyFailingSoftPVpcTimeStamp_Object=MibTableColumn
atmCurrentlyFailingSoftPVpcTimeStamp=_AtmCurrentlyFailingSoftPVpcTimeStamp_Object((1,3,6,1,4,1,353,5,5,1,1,6,1,1),_AtmCurrentlyFailingSoftPVpcTimeStamp_Type())
atmCurrentlyFailingSoftPVpcTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVpcTimeStamp.setStatus(_A)
_AtmSoftPvcMIBTraps_ObjectIdentity=ObjectIdentity
atmSoftPvcMIBTraps=_AtmSoftPvcMIBTraps_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,2))
_AtmSoftPvcTraps_ObjectIdentity=ObjectIdentity
atmSoftPvcTraps=_AtmSoftPvcTraps_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,2,1))
_AtmSoftPvcTrapsPrefix_ObjectIdentity=ObjectIdentity
atmSoftPvcTrapsPrefix=_AtmSoftPvcTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,2,1,0))
_AtmSoftPvcMIBConformance_ObjectIdentity=ObjectIdentity
atmSoftPvcMIBConformance=_AtmSoftPvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,3))
_AtmSoftPvcMIBCompliances_ObjectIdentity=ObjectIdentity
atmSoftPvcMIBCompliances=_AtmSoftPvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,3,1))
_AtmSoftPvcMIBGroups_ObjectIdentity=ObjectIdentity
atmSoftPvcMIBGroups=_AtmSoftPvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,353,5,5,1,3,2))
atmSoftPvcBaseMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,1))
atmSoftPvcBaseMIBGroup.setObjects(*((_B,_c),(_B,_P),(_B,_Q),(_B,_R),(_B,_d)))
if mibBuilder.loadTexts:atmSoftPvcBaseMIBGroup.setStatus(_A)
atmSoftPvcVccMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,2))
atmSoftPvcVccMIBGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:atmSoftPvcVccMIBGroup.setStatus(_A)
atmSoftPvcVpcMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,3))
atmSoftPvcVpcMIBGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:atmSoftPvcVpcMIBGroup.setStatus(_A)
atmSoftPvcAddressMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,4))
atmSoftPvcAddressMIBGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:atmSoftPvcAddressMIBGroup.setStatus(_A)
atmCurrentlyFailingSoftPVccMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,5))
atmCurrentlyFailingSoftPVccMIBGroup.setObjects((_B,_A6))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVccMIBGroup.setStatus(_A)
atmCurrentlyFailingSoftPVpcMIBGroup=ObjectGroup((1,3,6,1,4,1,353,5,5,1,3,2,6))
atmCurrentlyFailingSoftPVpcMIBGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:atmCurrentlyFailingSoftPVpcMIBGroup.setStatus(_A)
atmSoftPvcCallFailuresTrap=NotificationType((1,3,6,1,4,1,353,5,5,1,2,1,0,1))
atmSoftPvcCallFailuresTrap.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:atmSoftPvcCallFailuresTrap.setStatus(_A)
atmSoftPvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,353,5,5,1,3,1,1))
atmSoftPvcMIBCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:atmSoftPvcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtmAddr':AtmAddr,'atmForum':atmForum,'atmForumNetworkManagement':atmForumNetworkManagement,'atmfSoftPvc':atmfSoftPvc,'atmSoftPvcMIB':atmSoftPvcMIB,'atmSoftPvcMIBObjects':atmSoftPvcMIBObjects,'atmSoftPvcBaseGroup':atmSoftPvcBaseGroup,_c:atmSoftPvcCallFailuresTrapEnable,_P:atmSoftPvcCallFailures,_Q:atmSoftPvcCurrentlyFailingSoftPVccs,_R:atmSoftPvcCurrentlyFailingSoftPVpcs,_d:atmSoftPvcNotificationInterval,'atmSoftPVccTable':atmSoftPVccTable,'atmSoftPVccEntry':atmSoftPVccEntry,_M:atmSoftPVccLeafReference,_e:atmSoftPVccTargetAddress,_f:atmSoftPVccTargetSelectType,_g:atmSoftPVccTargetVpi,_h:atmSoftPVccTargetVci,_i:atmSoftPVccLastReleaseCause,_j:atmSoftPVccLastReleaseDiagnostic,_k:atmSoftPVccOperStatus,_l:atmSoftPVccRestart,_m:atmSoftPVccRetryInterval,_n:atmSoftPVccRetryTimer,_o:atmSoftPVccRetryThreshold,_p:atmSoftPVccRetryFailures,_q:atmSoftPVccRetryLimit,_r:atmSoftPVccRowStatus,'atmSoftPVpcTable':atmSoftPVpcTable,'atmSoftPVpcEntry':atmSoftPVpcEntry,_O:atmSoftPVpcLeafReference,_s:atmSoftPVpcTargetAddress,_t:atmSoftPVpcTargetSelectType,_u:atmSoftPVpcTargetVpi,_v:atmSoftPVpcLastReleaseCause,_w:atmSoftPVpcLastReleaseDiagnostic,_x:atmSoftPVpcOperStatus,_y:atmSoftPVpcRestart,_z:atmSoftPVpcRetryInterval,_A0:atmSoftPVpcRetryTimer,_A1:atmSoftPVpcRetryThreshold,_A2:atmSoftPVpcRetryFailures,_A3:atmSoftPVpcRetryLimit,_A4:atmSoftPVpcRowStatus,'atmInterfaceSoftPvcAddressTable':atmInterfaceSoftPvcAddressTable,'atmInterfaceSoftPvcAddressEntry':atmInterfaceSoftPvcAddressEntry,_b:atmInterfaceSoftPvcAddress,_A5:atmInterfaceSoftPvcAddressRowStatus,'atmCurrentlyFailingSoftPVccTable':atmCurrentlyFailingSoftPVccTable,'atmCurrentlyFailingSoftPVccEntry':atmCurrentlyFailingSoftPVccEntry,_A6:atmCurrentlyFailingSoftPVccTimeStamp,'atmCurrentlyFailingSoftPVpcTable':atmCurrentlyFailingSoftPVpcTable,'atmCurrentlyFailingSoftPVpcEntry':atmCurrentlyFailingSoftPVpcEntry,_A7:atmCurrentlyFailingSoftPVpcTimeStamp,'atmSoftPvcMIBTraps':atmSoftPvcMIBTraps,'atmSoftPvcTraps':atmSoftPvcTraps,'atmSoftPvcTrapsPrefix':atmSoftPvcTrapsPrefix,'atmSoftPvcCallFailuresTrap':atmSoftPvcCallFailuresTrap,'atmSoftPvcMIBConformance':atmSoftPvcMIBConformance,'atmSoftPvcMIBCompliances':atmSoftPvcMIBCompliances,'atmSoftPvcMIBCompliance':atmSoftPvcMIBCompliance,'atmSoftPvcMIBGroups':atmSoftPvcMIBGroups,_A8:atmSoftPvcBaseMIBGroup,_A9:atmSoftPvcVccMIBGroup,'atmSoftPvcVpcMIBGroup':atmSoftPvcVpcMIBGroup,_AA:atmSoftPvcAddressMIBGroup,'atmCurrentlyFailingSoftPVccMIBGroup':atmCurrentlyFailingSoftPVccMIBGroup,'atmCurrentlyFailingSoftPVpcMIBGroup':atmCurrentlyFailingSoftPVpcMIBGroup})