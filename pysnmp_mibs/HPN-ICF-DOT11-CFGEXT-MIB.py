_F='read-create'
_E='hpnicfDot11LBRadioGroupId'
_D='HPN-ICF-DOT11-CFGEXT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfDot11,=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB','hpnicfDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfDot11CFGEXT=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,6))
if mibBuilder.loadTexts:hpnicfDot11CFGEXT.setRevisions(('2010-06-02 14:00','2007-04-25 20:00'))
_HpnicfDot11LoadBalance_ObjectIdentity=ObjectIdentity
hpnicfDot11LoadBalance=_HpnicfDot11LoadBalance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1))
_HpnicfDot11LBGlobalGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11LBGlobalGroup=_HpnicfDot11LBGlobalGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1))
_HpnicfDot11LoadBalanceTrafficEnable_Type=TruthValue
_HpnicfDot11LoadBalanceTrafficEnable_Object=MibScalar
hpnicfDot11LoadBalanceTrafficEnable=_HpnicfDot11LoadBalanceTrafficEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,1),_HpnicfDot11LoadBalanceTrafficEnable_Type())
hpnicfDot11LoadBalanceTrafficEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceTrafficEnable.setStatus(_A)
_HpnicfDot11LoadBalanceTrafficThres_Type=Integer32
_HpnicfDot11LoadBalanceTrafficThres_Object=MibScalar
hpnicfDot11LoadBalanceTrafficThres=_HpnicfDot11LoadBalanceTrafficThres_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,2),_HpnicfDot11LoadBalanceTrafficThres_Type())
hpnicfDot11LoadBalanceTrafficThres.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceTrafficThres.setStatus(_A)
_HpnicfDot11LoadBalanceSessionEnable_Type=TruthValue
_HpnicfDot11LoadBalanceSessionEnable_Object=MibScalar
hpnicfDot11LoadBalanceSessionEnable=_HpnicfDot11LoadBalanceSessionEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,3),_HpnicfDot11LoadBalanceSessionEnable_Type())
hpnicfDot11LoadBalanceSessionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceSessionEnable.setStatus(_A)
_HpnicfDot11LoadBalanceSessionThres_Type=Integer32
_HpnicfDot11LoadBalanceSessionThres_Object=MibScalar
hpnicfDot11LoadBalanceSessionThres=_HpnicfDot11LoadBalanceSessionThres_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,4),_HpnicfDot11LoadBalanceSessionThres_Type())
hpnicfDot11LoadBalanceSessionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceSessionThres.setStatus(_A)
class _HpnicfDot11LoadBalanceTrafficGap_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,40))
_HpnicfDot11LoadBalanceTrafficGap_Type.__name__=_C
_HpnicfDot11LoadBalanceTrafficGap_Object=MibScalar
hpnicfDot11LoadBalanceTrafficGap=_HpnicfDot11LoadBalanceTrafficGap_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,5),_HpnicfDot11LoadBalanceTrafficGap_Type())
hpnicfDot11LoadBalanceTrafficGap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceTrafficGap.setStatus(_A)
class _HpnicfDot11LoadBalanceSessionGap_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfDot11LoadBalanceSessionGap_Type.__name__=_C
_HpnicfDot11LoadBalanceSessionGap_Object=MibScalar
hpnicfDot11LoadBalanceSessionGap=_HpnicfDot11LoadBalanceSessionGap_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,6),_HpnicfDot11LoadBalanceSessionGap_Type())
hpnicfDot11LoadBalanceSessionGap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LoadBalanceSessionGap.setStatus(_A)
_HpnicfDot11LBTrafficThresKbps_Type=Integer32
_HpnicfDot11LBTrafficThresKbps_Object=MibScalar
hpnicfDot11LBTrafficThresKbps=_HpnicfDot11LBTrafficThresKbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,7),_HpnicfDot11LBTrafficThresKbps_Type())
hpnicfDot11LBTrafficThresKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LBTrafficThresKbps.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11LBTrafficThresKbps.setUnits('kbps')
_HpnicfDot11LBTrafficGapKbps_Type=Integer32
_HpnicfDot11LBTrafficGapKbps_Object=MibScalar
hpnicfDot11LBTrafficGapKbps=_HpnicfDot11LBTrafficGapKbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,1,8),_HpnicfDot11LBTrafficGapKbps_Type())
hpnicfDot11LBTrafficGapKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11LBTrafficGapKbps.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11LBTrafficGapKbps.setUnits('kbps')
_HpnicfDot11LBRadioGroupTable_Object=MibTable
hpnicfDot11LBRadioGroupTable=_HpnicfDot11LBRadioGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,2))
if mibBuilder.loadTexts:hpnicfDot11LBRadioGroupTable.setStatus(_A)
_HpnicfDot11LBRadioGroupEntry_Object=MibTableRow
hpnicfDot11LBRadioGroupEntry=_HpnicfDot11LBRadioGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,2,1))
hpnicfDot11LBRadioGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfDot11LBRadioGroupEntry.setStatus(_A)
_HpnicfDot11LBRadioGroupId_Type=Unsigned32
_HpnicfDot11LBRadioGroupId_Object=MibTableColumn
hpnicfDot11LBRadioGroupId=_HpnicfDot11LBRadioGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,2,1,1),_HpnicfDot11LBRadioGroupId_Type())
hpnicfDot11LBRadioGroupId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfDot11LBRadioGroupId.setStatus(_A)
_HpnicfDot11LBRadioGroupDesc_Type=OctetString
_HpnicfDot11LBRadioGroupDesc_Object=MibTableColumn
hpnicfDot11LBRadioGroupDesc=_HpnicfDot11LBRadioGroupDesc_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,2,1,2),_HpnicfDot11LBRadioGroupDesc_Type())
hpnicfDot11LBRadioGroupDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11LBRadioGroupDesc.setStatus(_A)
_HpnicfDot11LBRadioGroupRowStatus_Type=RowStatus
_HpnicfDot11LBRadioGroupRowStatus_Object=MibTableColumn
hpnicfDot11LBRadioGroupRowStatus=_HpnicfDot11LBRadioGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,6,1,2,1,3),_HpnicfDot11LBRadioGroupRowStatus_Type())
hpnicfDot11LBRadioGroupRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11LBRadioGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfDot11CFGEXT':hpnicfDot11CFGEXT,'hpnicfDot11LoadBalance':hpnicfDot11LoadBalance,'hpnicfDot11LBGlobalGroup':hpnicfDot11LBGlobalGroup,'hpnicfDot11LoadBalanceTrafficEnable':hpnicfDot11LoadBalanceTrafficEnable,'hpnicfDot11LoadBalanceTrafficThres':hpnicfDot11LoadBalanceTrafficThres,'hpnicfDot11LoadBalanceSessionEnable':hpnicfDot11LoadBalanceSessionEnable,'hpnicfDot11LoadBalanceSessionThres':hpnicfDot11LoadBalanceSessionThres,'hpnicfDot11LoadBalanceTrafficGap':hpnicfDot11LoadBalanceTrafficGap,'hpnicfDot11LoadBalanceSessionGap':hpnicfDot11LoadBalanceSessionGap,'hpnicfDot11LBTrafficThresKbps':hpnicfDot11LBTrafficThresKbps,'hpnicfDot11LBTrafficGapKbps':hpnicfDot11LBTrafficGapKbps,'hpnicfDot11LBRadioGroupTable':hpnicfDot11LBRadioGroupTable,'hpnicfDot11LBRadioGroupEntry':hpnicfDot11LBRadioGroupEntry,_E:hpnicfDot11LBRadioGroupId,'hpnicfDot11LBRadioGroupDesc':hpnicfDot11LBRadioGroupDesc,'hpnicfDot11LBRadioGroupRowStatus':hpnicfDot11LBRadioGroupRowStatus})