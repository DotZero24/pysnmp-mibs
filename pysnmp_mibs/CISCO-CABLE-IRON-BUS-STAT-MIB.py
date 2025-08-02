_U='ciscoCableIronBusStatObjectGroup'
_T='ciscoCableIronBusStatMessageIntervalDefault'
_S='ciscoCableIronBusStatTibBandwidth'
_R='ciscoCableIronBusStatTibPktPerSec'
_Q='ciscoCableIronBusStatFibPktsPerSec'
_P='ciscoCableIronBusStatTibByteSent'
_O='ciscoCableIronBusStatTibPktsSent'
_N='ciscoCableIronBusStatFibBytesRcv'
_M='ciscoCableIronBusStatFibPktsRcv'
_L='ciscoCableIronBusStatBandwidthDefault'
_K='ciscoCableIronBusStatBandwidthCurrent'
_J='ciscoCableIronBusStatMessageIntervalCurrent'
_I='ciscoCableIronBusStatFibBandwidth'
_H='minutes'
_G='read-write'
_F='ciscoCableIronBusStatIndex'
_E='Integer32'
_D='NonZeroPercent'
_C='read-only'
_B='CISCO-CABLE-IRON-BUS-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NonZeroPercent,=mibBuilder.importSymbols('CISCO-CABLE-ADMISSION-CTRL-MIB',_D)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCableIronBusStatMIB=ModuleIdentity((1,3,6,1,4,1,9,9,821))
if mibBuilder.loadTexts:ciscoCableIronBusStatMIB.setRevisions(('2014-08-14 00:00',))
_CiscoCableIronBusStatMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCableIronBusStatMIBNotifs=_CiscoCableIronBusStatMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,821,0))
_CiscoCableIronBusStatMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableIronBusStatMIBObjects=_CiscoCableIronBusStatMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,821,1))
_CiscoCableIronBusStatTable_Object=MibTable
ciscoCableIronBusStatTable=_CiscoCableIronBusStatTable_Object((1,3,6,1,4,1,9,9,821,1,1))
if mibBuilder.loadTexts:ciscoCableIronBusStatTable.setStatus(_A)
_CiscoCableIronBusStatEntry_Object=MibTableRow
ciscoCableIronBusStatEntry=_CiscoCableIronBusStatEntry_Object((1,3,6,1,4,1,9,9,821,1,1,1))
ciscoCableIronBusStatEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoCableIronBusStatEntry.setStatus(_A)
_CiscoCableIronBusStatIndex_Type=Integer32
_CiscoCableIronBusStatIndex_Object=MibTableColumn
ciscoCableIronBusStatIndex=_CiscoCableIronBusStatIndex_Object((1,3,6,1,4,1,9,9,821,1,1,1,1),_CiscoCableIronBusStatIndex_Type())
ciscoCableIronBusStatIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoCableIronBusStatIndex.setStatus(_A)
class _CiscoCableIronBusStatFibBandwidth_Type(NonZeroPercent):subtypeSpec=NonZeroPercent.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoCableIronBusStatFibBandwidth_Type.__name__=_D
_CiscoCableIronBusStatFibBandwidth_Object=MibTableColumn
ciscoCableIronBusStatFibBandwidth=_CiscoCableIronBusStatFibBandwidth_Object((1,3,6,1,4,1,9,9,821,1,1,1,2),_CiscoCableIronBusStatFibBandwidth_Type())
ciscoCableIronBusStatFibBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatFibBandwidth.setStatus(_A)
class _CiscoCableIronBusStatTibBandwidth_Type(NonZeroPercent):subtypeSpec=NonZeroPercent.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoCableIronBusStatTibBandwidth_Type.__name__=_D
_CiscoCableIronBusStatTibBandwidth_Object=MibTableColumn
ciscoCableIronBusStatTibBandwidth=_CiscoCableIronBusStatTibBandwidth_Object((1,3,6,1,4,1,9,9,821,1,1,1,3),_CiscoCableIronBusStatTibBandwidth_Type())
ciscoCableIronBusStatTibBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatTibBandwidth.setStatus(_A)
class _CiscoCableIronBusStatMessageIntervalCurrent_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CiscoCableIronBusStatMessageIntervalCurrent_Type.__name__=_E
_CiscoCableIronBusStatMessageIntervalCurrent_Object=MibTableColumn
ciscoCableIronBusStatMessageIntervalCurrent=_CiscoCableIronBusStatMessageIntervalCurrent_Object((1,3,6,1,4,1,9,9,821,1,1,1,4),_CiscoCableIronBusStatMessageIntervalCurrent_Type())
ciscoCableIronBusStatMessageIntervalCurrent.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoCableIronBusStatMessageIntervalCurrent.setStatus(_A)
if mibBuilder.loadTexts:ciscoCableIronBusStatMessageIntervalCurrent.setUnits(_H)
class _CiscoCableIronBusStatBandwidthCurrent_Type(NonZeroPercent):defaultValue=90;subtypeSpec=NonZeroPercent.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,100))
_CiscoCableIronBusStatBandwidthCurrent_Type.__name__=_D
_CiscoCableIronBusStatBandwidthCurrent_Object=MibTableColumn
ciscoCableIronBusStatBandwidthCurrent=_CiscoCableIronBusStatBandwidthCurrent_Object((1,3,6,1,4,1,9,9,821,1,1,1,5),_CiscoCableIronBusStatBandwidthCurrent_Type())
ciscoCableIronBusStatBandwidthCurrent.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoCableIronBusStatBandwidthCurrent.setStatus(_A)
class _CiscoCableIronBusStatMessageIntervalDefault_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CiscoCableIronBusStatMessageIntervalDefault_Type.__name__=_E
_CiscoCableIronBusStatMessageIntervalDefault_Object=MibTableColumn
ciscoCableIronBusStatMessageIntervalDefault=_CiscoCableIronBusStatMessageIntervalDefault_Object((1,3,6,1,4,1,9,9,821,1,1,1,6),_CiscoCableIronBusStatMessageIntervalDefault_Type())
ciscoCableIronBusStatMessageIntervalDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatMessageIntervalDefault.setStatus(_A)
if mibBuilder.loadTexts:ciscoCableIronBusStatMessageIntervalDefault.setUnits(_H)
class _CiscoCableIronBusStatBandwidthDefault_Type(NonZeroPercent):defaultValue=90;subtypeSpec=NonZeroPercent.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoCableIronBusStatBandwidthDefault_Type.__name__=_D
_CiscoCableIronBusStatBandwidthDefault_Object=MibTableColumn
ciscoCableIronBusStatBandwidthDefault=_CiscoCableIronBusStatBandwidthDefault_Object((1,3,6,1,4,1,9,9,821,1,1,1,7),_CiscoCableIronBusStatBandwidthDefault_Type())
ciscoCableIronBusStatBandwidthDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatBandwidthDefault.setStatus(_A)
_CiscoCableIronBusStatFibPktsRcv_Type=Counter64
_CiscoCableIronBusStatFibPktsRcv_Object=MibTableColumn
ciscoCableIronBusStatFibPktsRcv=_CiscoCableIronBusStatFibPktsRcv_Object((1,3,6,1,4,1,9,9,821,1,1,1,8),_CiscoCableIronBusStatFibPktsRcv_Type())
ciscoCableIronBusStatFibPktsRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatFibPktsRcv.setStatus(_A)
_CiscoCableIronBusStatFibBytesRcv_Type=Counter64
_CiscoCableIronBusStatFibBytesRcv_Object=MibTableColumn
ciscoCableIronBusStatFibBytesRcv=_CiscoCableIronBusStatFibBytesRcv_Object((1,3,6,1,4,1,9,9,821,1,1,1,9),_CiscoCableIronBusStatFibBytesRcv_Type())
ciscoCableIronBusStatFibBytesRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatFibBytesRcv.setStatus(_A)
_CiscoCableIronBusStatTibPktsSent_Type=Counter64
_CiscoCableIronBusStatTibPktsSent_Object=MibTableColumn
ciscoCableIronBusStatTibPktsSent=_CiscoCableIronBusStatTibPktsSent_Object((1,3,6,1,4,1,9,9,821,1,1,1,10),_CiscoCableIronBusStatTibPktsSent_Type())
ciscoCableIronBusStatTibPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatTibPktsSent.setStatus(_A)
_CiscoCableIronBusStatTibByteSent_Type=Counter64
_CiscoCableIronBusStatTibByteSent_Object=MibTableColumn
ciscoCableIronBusStatTibByteSent=_CiscoCableIronBusStatTibByteSent_Object((1,3,6,1,4,1,9,9,821,1,1,1,11),_CiscoCableIronBusStatTibByteSent_Type())
ciscoCableIronBusStatTibByteSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatTibByteSent.setStatus(_A)
_CiscoCableIronBusStatFibPktsPerSec_Type=Counter64
_CiscoCableIronBusStatFibPktsPerSec_Object=MibTableColumn
ciscoCableIronBusStatFibPktsPerSec=_CiscoCableIronBusStatFibPktsPerSec_Object((1,3,6,1,4,1,9,9,821,1,1,1,12),_CiscoCableIronBusStatFibPktsPerSec_Type())
ciscoCableIronBusStatFibPktsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatFibPktsPerSec.setStatus(_A)
_CiscoCableIronBusStatTibPktPerSec_Type=Counter64
_CiscoCableIronBusStatTibPktPerSec_Object=MibTableColumn
ciscoCableIronBusStatTibPktPerSec=_CiscoCableIronBusStatTibPktPerSec_Object((1,3,6,1,4,1,9,9,821,1,1,1,13),_CiscoCableIronBusStatTibPktPerSec_Type())
ciscoCableIronBusStatTibPktPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCableIronBusStatTibPktPerSec.setStatus(_A)
_CiscoCableIronBusStatMIBConform_ObjectIdentity=ObjectIdentity
ciscoCableIronBusStatMIBConform=_CiscoCableIronBusStatMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,821,2))
_CiscoCableIronBusStatMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCableIronBusStatMIBCompliances=_CiscoCableIronBusStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,821,2,1))
_CiscoCableIronBusStatMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCableIronBusStatMIBGroups=_CiscoCableIronBusStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,821,2,2))
ciscoCableIronBusStatObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,821,2,2,1))
ciscoCableIronBusStatObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoCableIronBusStatObjectGroup.setStatus(_A)
ciscoCableIronBusStatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,821,2,1,1))
ciscoCableIronBusStatMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoCableIronBusStatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCableIronBusStatMIB':ciscoCableIronBusStatMIB,'ciscoCableIronBusStatMIBNotifs':ciscoCableIronBusStatMIBNotifs,'ciscoCableIronBusStatMIBObjects':ciscoCableIronBusStatMIBObjects,'ciscoCableIronBusStatTable':ciscoCableIronBusStatTable,'ciscoCableIronBusStatEntry':ciscoCableIronBusStatEntry,_F:ciscoCableIronBusStatIndex,_I:ciscoCableIronBusStatFibBandwidth,_S:ciscoCableIronBusStatTibBandwidth,_J:ciscoCableIronBusStatMessageIntervalCurrent,_K:ciscoCableIronBusStatBandwidthCurrent,_T:ciscoCableIronBusStatMessageIntervalDefault,_L:ciscoCableIronBusStatBandwidthDefault,_M:ciscoCableIronBusStatFibPktsRcv,_N:ciscoCableIronBusStatFibBytesRcv,_O:ciscoCableIronBusStatTibPktsSent,_P:ciscoCableIronBusStatTibByteSent,_Q:ciscoCableIronBusStatFibPktsPerSec,_R:ciscoCableIronBusStatTibPktPerSec,'ciscoCableIronBusStatMIBConform':ciscoCableIronBusStatMIBConform,'ciscoCableIronBusStatMIBCompliances':ciscoCableIronBusStatMIBCompliances,'ciscoCableIronBusStatMIBCompliance':ciscoCableIronBusStatMIBCompliance,'ciscoCableIronBusStatMIBGroups':ciscoCableIronBusStatMIBGroups,_U:ciscoCableIronBusStatObjectGroup})