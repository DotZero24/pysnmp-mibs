_Q='jnxFWCntrXEntry'
_P='jnxFWCounterType'
_O='jnxFWCounterName'
_N='jnxFWCounterFilterName'
_M='jnxFWCounter'
_L='jnxFWFilter'
_K='not-accessible'
_J='hpolpre'
_I='hpolagg'
_H='policer'
_G='counter'
_F='other'
_E='Integer32'
_D='JUNIPER-FIREWALL-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
jnxFirewalls=ModuleIdentity((1,3,6,1,4,1,2636,3,5))
if mibBuilder.loadTexts:jnxFirewalls.setRevisions(('2016-01-23 15:53',))
_JnxFirewallsTable_Object=MibTable
jnxFirewallsTable=_JnxFirewallsTable_Object((1,3,6,1,4,1,2636,3,5,1))
if mibBuilder.loadTexts:jnxFirewallsTable.setStatus('deprecated')
_JnxFirewallsEntry_Object=MibTableRow
jnxFirewallsEntry=_JnxFirewallsEntry_Object((1,3,6,1,4,1,2636,3,5,1,1))
jnxFirewallsEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:jnxFirewallsEntry.setStatus(_A)
class _JnxFWFilter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_JnxFWFilter_Type.__name__=_C
_JnxFWFilter_Object=MibTableColumn
jnxFWFilter=_JnxFWFilter_Object((1,3,6,1,4,1,2636,3,5,1,1,1),_JnxFWFilter_Type())
jnxFWFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWFilter.setStatus(_A)
class _JnxFWCounter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_JnxFWCounter_Type.__name__=_C
_JnxFWCounter_Object=MibTableColumn
jnxFWCounter=_JnxFWCounter_Object((1,3,6,1,4,1,2636,3,5,1,1,2),_JnxFWCounter_Type())
jnxFWCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounter.setStatus(_A)
class _JnxFWType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_JnxFWType_Type.__name__=_E
_JnxFWType_Object=MibTableColumn
jnxFWType=_JnxFWType_Object((1,3,6,1,4,1,2636,3,5,1,1,3),_JnxFWType_Type())
jnxFWType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWType.setStatus(_A)
_JnxFWPackets_Type=Counter64
_JnxFWPackets_Object=MibTableColumn
jnxFWPackets=_JnxFWPackets_Object((1,3,6,1,4,1,2636,3,5,1,1,4),_JnxFWPackets_Type())
jnxFWPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWPackets.setStatus(_A)
_JnxFWBytes_Type=Counter64
_JnxFWBytes_Object=MibTableColumn
jnxFWBytes=_JnxFWBytes_Object((1,3,6,1,4,1,2636,3,5,1,1,5),_JnxFWBytes_Type())
jnxFWBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWBytes.setStatus(_A)
_JnxFirewallCounterTable_Object=MibTable
jnxFirewallCounterTable=_JnxFirewallCounterTable_Object((1,3,6,1,4,1,2636,3,5,2))
if mibBuilder.loadTexts:jnxFirewallCounterTable.setStatus(_A)
_JnxFirewallCounterEntry_Object=MibTableRow
jnxFirewallCounterEntry=_JnxFirewallCounterEntry_Object((1,3,6,1,4,1,2636,3,5,2,1))
jnxFirewallCounterEntry.setIndexNames((0,_D,_N),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:jnxFirewallCounterEntry.setStatus(_A)
class _JnxFWCounterFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JnxFWCounterFilterName_Type.__name__=_C
_JnxFWCounterFilterName_Object=MibTableColumn
jnxFWCounterFilterName=_JnxFWCounterFilterName_Object((1,3,6,1,4,1,2636,3,5,2,1,1),_JnxFWCounterFilterName_Type())
jnxFWCounterFilterName.setMaxAccess(_K)
if mibBuilder.loadTexts:jnxFWCounterFilterName.setStatus(_A)
class _JnxFWCounterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JnxFWCounterName_Type.__name__=_C
_JnxFWCounterName_Object=MibTableColumn
jnxFWCounterName=_JnxFWCounterName_Object((1,3,6,1,4,1,2636,3,5,2,1,2),_JnxFWCounterName_Type())
jnxFWCounterName.setMaxAccess(_K)
if mibBuilder.loadTexts:jnxFWCounterName.setStatus(_A)
class _JnxFWCounterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_JnxFWCounterType_Type.__name__=_E
_JnxFWCounterType_Object=MibTableColumn
jnxFWCounterType=_JnxFWCounterType_Object((1,3,6,1,4,1,2636,3,5,2,1,3),_JnxFWCounterType_Type())
jnxFWCounterType.setMaxAccess(_K)
if mibBuilder.loadTexts:jnxFWCounterType.setStatus(_A)
_JnxFWCounterPacketCount_Type=Counter64
_JnxFWCounterPacketCount_Object=MibTableColumn
jnxFWCounterPacketCount=_JnxFWCounterPacketCount_Object((1,3,6,1,4,1,2636,3,5,2,1,4),_JnxFWCounterPacketCount_Type())
jnxFWCounterPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounterPacketCount.setStatus(_A)
_JnxFWCounterByteCount_Type=Counter64
_JnxFWCounterByteCount_Object=MibTableColumn
jnxFWCounterByteCount=_JnxFWCounterByteCount_Object((1,3,6,1,4,1,2636,3,5,2,1,5),_JnxFWCounterByteCount_Type())
jnxFWCounterByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounterByteCount.setStatus(_A)
class _JnxFWCounterDisplayFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JnxFWCounterDisplayFilterName_Type.__name__=_C
_JnxFWCounterDisplayFilterName_Object=MibTableColumn
jnxFWCounterDisplayFilterName=_JnxFWCounterDisplayFilterName_Object((1,3,6,1,4,1,2636,3,5,2,1,6),_JnxFWCounterDisplayFilterName_Type())
jnxFWCounterDisplayFilterName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounterDisplayFilterName.setStatus(_A)
class _JnxFWCounterDisplayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_JnxFWCounterDisplayName_Type.__name__=_C
_JnxFWCounterDisplayName_Object=MibTableColumn
jnxFWCounterDisplayName=_JnxFWCounterDisplayName_Object((1,3,6,1,4,1,2636,3,5,2,1,7),_JnxFWCounterDisplayName_Type())
jnxFWCounterDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounterDisplayName.setStatus(_A)
class _JnxFWCounterDisplayType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_J,5)))
_JnxFWCounterDisplayType_Type.__name__=_E
_JnxFWCounterDisplayType_Object=MibTableColumn
jnxFWCounterDisplayType=_JnxFWCounterDisplayType_Object((1,3,6,1,4,1,2636,3,5,2,1,8),_JnxFWCounterDisplayType_Type())
jnxFWCounterDisplayType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCounterDisplayType.setStatus(_A)
_JnxFWCntrXTable_Object=MibTable
jnxFWCntrXTable=_JnxFWCntrXTable_Object((1,3,6,1,4,1,2636,3,5,3))
if mibBuilder.loadTexts:jnxFWCntrXTable.setStatus(_A)
_JnxFWCntrXEntry_Object=MibTableRow
jnxFWCntrXEntry=_JnxFWCntrXEntry_Object((1,3,6,1,4,1,2636,3,5,3,1))
if mibBuilder.loadTexts:jnxFWCntrXEntry.setStatus(_A)
_JnxFWCntrPolicerOfferedPktCount_Type=Counter64
_JnxFWCntrPolicerOfferedPktCount_Object=MibTableColumn
jnxFWCntrPolicerOfferedPktCount=_JnxFWCntrPolicerOfferedPktCount_Object((1,3,6,1,4,1,2636,3,5,3,1,1),_JnxFWCntrPolicerOfferedPktCount_Type())
jnxFWCntrPolicerOfferedPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerOfferedPktCount.setStatus(_A)
_JnxFWCntrPolicerOfferedByteCount_Type=Counter64
_JnxFWCntrPolicerOfferedByteCount_Object=MibTableColumn
jnxFWCntrPolicerOfferedByteCount=_JnxFWCntrPolicerOfferedByteCount_Object((1,3,6,1,4,1,2636,3,5,3,1,2),_JnxFWCntrPolicerOfferedByteCount_Type())
jnxFWCntrPolicerOfferedByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerOfferedByteCount.setStatus(_A)
_JnxFWCntrPolicerOutSpecPktCount_Type=Counter64
_JnxFWCntrPolicerOutSpecPktCount_Object=MibTableColumn
jnxFWCntrPolicerOutSpecPktCount=_JnxFWCntrPolicerOutSpecPktCount_Object((1,3,6,1,4,1,2636,3,5,3,1,3),_JnxFWCntrPolicerOutSpecPktCount_Type())
jnxFWCntrPolicerOutSpecPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerOutSpecPktCount.setStatus(_A)
_JnxFWCntrPolicerOutSpecByteCount_Type=Counter64
_JnxFWCntrPolicerOutSpecByteCount_Object=MibTableColumn
jnxFWCntrPolicerOutSpecByteCount=_JnxFWCntrPolicerOutSpecByteCount_Object((1,3,6,1,4,1,2636,3,5,3,1,4),_JnxFWCntrPolicerOutSpecByteCount_Type())
jnxFWCntrPolicerOutSpecByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerOutSpecByteCount.setStatus(_A)
_JnxFWCntrPolicerTxPktCount_Type=Counter64
_JnxFWCntrPolicerTxPktCount_Object=MibTableColumn
jnxFWCntrPolicerTxPktCount=_JnxFWCntrPolicerTxPktCount_Object((1,3,6,1,4,1,2636,3,5,3,1,5),_JnxFWCntrPolicerTxPktCount_Type())
jnxFWCntrPolicerTxPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerTxPktCount.setStatus(_A)
_JnxFWCntrPolicerTxByteCount_Type=Counter64
_JnxFWCntrPolicerTxByteCount_Object=MibTableColumn
jnxFWCntrPolicerTxByteCount=_JnxFWCntrPolicerTxByteCount_Object((1,3,6,1,4,1,2636,3,5,3,1,6),_JnxFWCntrPolicerTxByteCount_Type())
jnxFWCntrPolicerTxByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxFWCntrPolicerTxByteCount.setStatus(_A)
jnxFirewallCounterEntry.registerAugmentions((_D,_Q))
jnxFWCntrXEntry.setIndexNames(*jnxFirewallCounterEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'jnxFirewalls':jnxFirewalls,'jnxFirewallsTable':jnxFirewallsTable,'jnxFirewallsEntry':jnxFirewallsEntry,_L:jnxFWFilter,_M:jnxFWCounter,'jnxFWType':jnxFWType,'jnxFWPackets':jnxFWPackets,'jnxFWBytes':jnxFWBytes,'jnxFirewallCounterTable':jnxFirewallCounterTable,'jnxFirewallCounterEntry':jnxFirewallCounterEntry,_N:jnxFWCounterFilterName,_O:jnxFWCounterName,_P:jnxFWCounterType,'jnxFWCounterPacketCount':jnxFWCounterPacketCount,'jnxFWCounterByteCount':jnxFWCounterByteCount,'jnxFWCounterDisplayFilterName':jnxFWCounterDisplayFilterName,'jnxFWCounterDisplayName':jnxFWCounterDisplayName,'jnxFWCounterDisplayType':jnxFWCounterDisplayType,'jnxFWCntrXTable':jnxFWCntrXTable,_Q:jnxFWCntrXEntry,'jnxFWCntrPolicerOfferedPktCount':jnxFWCntrPolicerOfferedPktCount,'jnxFWCntrPolicerOfferedByteCount':jnxFWCntrPolicerOfferedByteCount,'jnxFWCntrPolicerOutSpecPktCount':jnxFWCntrPolicerOutSpecPktCount,'jnxFWCntrPolicerOutSpecByteCount':jnxFWCntrPolicerOutSpecByteCount,'jnxFWCntrPolicerTxPktCount':jnxFWCntrPolicerTxPktCount,'jnxFWCntrPolicerTxByteCount':jnxFWCntrPolicerTxByteCount})