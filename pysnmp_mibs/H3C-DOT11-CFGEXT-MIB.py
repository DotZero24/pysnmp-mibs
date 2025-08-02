_F='read-create'
_E='h3cDot11LBRadioGroupId'
_D='H3C-DOT11-CFGEXT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cDot11,=mibBuilder.importSymbols('H3C-DOT11-REF-MIB','h3cDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cDot11CFGEXT=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,6))
if mibBuilder.loadTexts:h3cDot11CFGEXT.setRevisions(('2016-03-11 18:00','2010-06-02 14:00','2007-04-25 20:00'))
_H3cDot11LoadBalance_ObjectIdentity=ObjectIdentity
h3cDot11LoadBalance=_H3cDot11LoadBalance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,6,1))
_H3cDot11LBGlobalGroup_ObjectIdentity=ObjectIdentity
h3cDot11LBGlobalGroup=_H3cDot11LBGlobalGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,6,1,1))
_H3cDot11LoadBalanceTrafficEnable_Type=TruthValue
_H3cDot11LoadBalanceTrafficEnable_Object=MibScalar
h3cDot11LoadBalanceTrafficEnable=_H3cDot11LoadBalanceTrafficEnable_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,1),_H3cDot11LoadBalanceTrafficEnable_Type())
h3cDot11LoadBalanceTrafficEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceTrafficEnable.setStatus(_A)
_H3cDot11LoadBalanceTrafficThres_Type=Integer32
_H3cDot11LoadBalanceTrafficThres_Object=MibScalar
h3cDot11LoadBalanceTrafficThres=_H3cDot11LoadBalanceTrafficThres_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,2),_H3cDot11LoadBalanceTrafficThres_Type())
h3cDot11LoadBalanceTrafficThres.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceTrafficThres.setStatus(_A)
_H3cDot11LoadBalanceSessionEnable_Type=TruthValue
_H3cDot11LoadBalanceSessionEnable_Object=MibScalar
h3cDot11LoadBalanceSessionEnable=_H3cDot11LoadBalanceSessionEnable_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,3),_H3cDot11LoadBalanceSessionEnable_Type())
h3cDot11LoadBalanceSessionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceSessionEnable.setStatus(_A)
_H3cDot11LoadBalanceSessionThres_Type=Integer32
_H3cDot11LoadBalanceSessionThres_Object=MibScalar
h3cDot11LoadBalanceSessionThres=_H3cDot11LoadBalanceSessionThres_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,4),_H3cDot11LoadBalanceSessionThres_Type())
h3cDot11LoadBalanceSessionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceSessionThres.setStatus(_A)
class _H3cDot11LoadBalanceTrafficGap_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,40))
_H3cDot11LoadBalanceTrafficGap_Type.__name__=_C
_H3cDot11LoadBalanceTrafficGap_Object=MibScalar
h3cDot11LoadBalanceTrafficGap=_H3cDot11LoadBalanceTrafficGap_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,5),_H3cDot11LoadBalanceTrafficGap_Type())
h3cDot11LoadBalanceTrafficGap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceTrafficGap.setStatus(_A)
class _H3cDot11LoadBalanceSessionGap_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cDot11LoadBalanceSessionGap_Type.__name__=_C
_H3cDot11LoadBalanceSessionGap_Object=MibScalar
h3cDot11LoadBalanceSessionGap=_H3cDot11LoadBalanceSessionGap_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,6),_H3cDot11LoadBalanceSessionGap_Type())
h3cDot11LoadBalanceSessionGap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceSessionGap.setStatus(_A)
_H3cDot11LBTrafficThresKbps_Type=Integer32
_H3cDot11LBTrafficThresKbps_Object=MibScalar
h3cDot11LBTrafficThresKbps=_H3cDot11LBTrafficThresKbps_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,7),_H3cDot11LBTrafficThresKbps_Type())
h3cDot11LBTrafficThresKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LBTrafficThresKbps.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LBTrafficThresKbps.setUnits('kbps')
_H3cDot11LBTrafficGapKbps_Type=Integer32
_H3cDot11LBTrafficGapKbps_Object=MibScalar
h3cDot11LBTrafficGapKbps=_H3cDot11LBTrafficGapKbps_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,8),_H3cDot11LBTrafficGapKbps_Type())
h3cDot11LBTrafficGapKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LBTrafficGapKbps.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11LBTrafficGapKbps.setUnits('kbps')
class _H3cDot11LoadBalanceEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('trafficBased',1),('userBased',2)))
_H3cDot11LoadBalanceEnable_Type.__name__=_C
_H3cDot11LoadBalanceEnable_Object=MibScalar
h3cDot11LoadBalanceEnable=_H3cDot11LoadBalanceEnable_Object((1,3,6,1,4,1,2011,10,2,75,6,1,1,9),_H3cDot11LoadBalanceEnable_Type())
h3cDot11LoadBalanceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11LoadBalanceEnable.setStatus(_A)
_H3cDot11LBRadioGroupTable_Object=MibTable
h3cDot11LBRadioGroupTable=_H3cDot11LBRadioGroupTable_Object((1,3,6,1,4,1,2011,10,2,75,6,1,2))
if mibBuilder.loadTexts:h3cDot11LBRadioGroupTable.setStatus(_A)
_H3cDot11LBRadioGroupEntry_Object=MibTableRow
h3cDot11LBRadioGroupEntry=_H3cDot11LBRadioGroupEntry_Object((1,3,6,1,4,1,2011,10,2,75,6,1,2,1))
h3cDot11LBRadioGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cDot11LBRadioGroupEntry.setStatus(_A)
_H3cDot11LBRadioGroupId_Type=Unsigned32
_H3cDot11LBRadioGroupId_Object=MibTableColumn
h3cDot11LBRadioGroupId=_H3cDot11LBRadioGroupId_Object((1,3,6,1,4,1,2011,10,2,75,6,1,2,1,1),_H3cDot11LBRadioGroupId_Type())
h3cDot11LBRadioGroupId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cDot11LBRadioGroupId.setStatus(_A)
_H3cDot11LBRadioGroupDesc_Type=OctetString
_H3cDot11LBRadioGroupDesc_Object=MibTableColumn
h3cDot11LBRadioGroupDesc=_H3cDot11LBRadioGroupDesc_Object((1,3,6,1,4,1,2011,10,2,75,6,1,2,1,2),_H3cDot11LBRadioGroupDesc_Type())
h3cDot11LBRadioGroupDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11LBRadioGroupDesc.setStatus(_A)
_H3cDot11LBRadioGroupRowStatus_Type=RowStatus
_H3cDot11LBRadioGroupRowStatus_Object=MibTableColumn
h3cDot11LBRadioGroupRowStatus=_H3cDot11LBRadioGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,6,1,2,1,3),_H3cDot11LBRadioGroupRowStatus_Type())
h3cDot11LBRadioGroupRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11LBRadioGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cDot11CFGEXT':h3cDot11CFGEXT,'h3cDot11LoadBalance':h3cDot11LoadBalance,'h3cDot11LBGlobalGroup':h3cDot11LBGlobalGroup,'h3cDot11LoadBalanceTrafficEnable':h3cDot11LoadBalanceTrafficEnable,'h3cDot11LoadBalanceTrafficThres':h3cDot11LoadBalanceTrafficThres,'h3cDot11LoadBalanceSessionEnable':h3cDot11LoadBalanceSessionEnable,'h3cDot11LoadBalanceSessionThres':h3cDot11LoadBalanceSessionThres,'h3cDot11LoadBalanceTrafficGap':h3cDot11LoadBalanceTrafficGap,'h3cDot11LoadBalanceSessionGap':h3cDot11LoadBalanceSessionGap,'h3cDot11LBTrafficThresKbps':h3cDot11LBTrafficThresKbps,'h3cDot11LBTrafficGapKbps':h3cDot11LBTrafficGapKbps,'h3cDot11LoadBalanceEnable':h3cDot11LoadBalanceEnable,'h3cDot11LBRadioGroupTable':h3cDot11LBRadioGroupTable,'h3cDot11LBRadioGroupEntry':h3cDot11LBRadioGroupEntry,_E:h3cDot11LBRadioGroupId,'h3cDot11LBRadioGroupDesc':h3cDot11LBRadioGroupDesc,'h3cDot11LBRadioGroupRowStatus':h3cDot11LBRadioGroupRowStatus})