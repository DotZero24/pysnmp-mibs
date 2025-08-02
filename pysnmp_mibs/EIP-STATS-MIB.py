_H='eipDhcp6StatName'
_G='eipDnsStatName'
_F='eipDhcpStatName'
_E='NotificationType'
_D='EIP-STATS-MIB'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Eip_ObjectIdentity=ObjectIdentity
eip=_Eip_ObjectIdentity((1,3,6,1,4,1,2440))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2440,1))
_EipDhcp_ObjectIdentity=ObjectIdentity
eipDhcp=_EipDhcp_ObjectIdentity((1,3,6,1,4,1,2440,1,3))
_EipDhcpStat_ObjectIdentity=ObjectIdentity
eipDhcpStat=_EipDhcpStat_ObjectIdentity((1,3,6,1,4,1,2440,1,3,2))
_EipDhcpStatTable_Object=MibTable
eipDhcpStatTable=_EipDhcpStatTable_Object((1,3,6,1,4,1,2440,1,3,2,22))
if mibBuilder.loadTexts:eipDhcpStatTable.setStatus(_A)
_EipDhcpStatEntry_Object=MibTableRow
eipDhcpStatEntry=_EipDhcpStatEntry_Object((1,3,6,1,4,1,2440,1,3,2,22,1))
eipDhcpStatEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:eipDhcpStatEntry.setStatus(_A)
class _EipDhcpStatIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDhcpStatIndex_Type.__name__=_C
_EipDhcpStatIndex_Object=MibTableColumn
eipDhcpStatIndex=_EipDhcpStatIndex_Object((1,3,6,1,4,1,2440,1,3,2,22,1,1),_EipDhcpStatIndex_Type())
eipDhcpStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcpStatIndex.setStatus(_A)
class _EipDhcpStatName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDhcpStatName_Type.__name__=_C
_EipDhcpStatName_Object=MibTableColumn
eipDhcpStatName=_EipDhcpStatName_Object((1,3,6,1,4,1,2440,1,3,2,22,1,2),_EipDhcpStatName_Type())
eipDhcpStatName.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcpStatName.setStatus(_A)
_EipDhcpStatValue_Type=Integer32
_EipDhcpStatValue_Object=MibTableColumn
eipDhcpStatValue=_EipDhcpStatValue_Object((1,3,6,1,4,1,2440,1,3,2,22,1,3),_EipDhcpStatValue_Type())
eipDhcpStatValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcpStatValue.setStatus(_A)
_EipDns_ObjectIdentity=ObjectIdentity
eipDns=_EipDns_ObjectIdentity((1,3,6,1,4,1,2440,1,4))
_EipDnsStat_ObjectIdentity=ObjectIdentity
eipDnsStat=_EipDnsStat_ObjectIdentity((1,3,6,1,4,1,2440,1,4,2))
_EipDnsStatTable_Object=MibTable
eipDnsStatTable=_EipDnsStatTable_Object((1,3,6,1,4,1,2440,1,4,2,3))
if mibBuilder.loadTexts:eipDnsStatTable.setStatus(_A)
_EipDnsStatEntry_Object=MibTableRow
eipDnsStatEntry=_EipDnsStatEntry_Object((1,3,6,1,4,1,2440,1,4,2,3,1))
eipDnsStatEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:eipDnsStatEntry.setStatus(_A)
class _EipDnsStatIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDnsStatIndex_Type.__name__=_C
_EipDnsStatIndex_Object=MibTableColumn
eipDnsStatIndex=_EipDnsStatIndex_Object((1,3,6,1,4,1,2440,1,4,2,3,1,1),_EipDnsStatIndex_Type())
eipDnsStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDnsStatIndex.setStatus(_A)
class _EipDnsStatName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDnsStatName_Type.__name__=_C
_EipDnsStatName_Object=MibTableColumn
eipDnsStatName=_EipDnsStatName_Object((1,3,6,1,4,1,2440,1,4,2,3,1,2),_EipDnsStatName_Type())
eipDnsStatName.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDnsStatName.setStatus(_A)
_EipDnsStatValue_Type=Integer32
_EipDnsStatValue_Object=MibTableColumn
eipDnsStatValue=_EipDnsStatValue_Object((1,3,6,1,4,1,2440,1,4,2,3,1,3),_EipDnsStatValue_Type())
eipDnsStatValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDnsStatValue.setStatus(_A)
_EipDhcp6_ObjectIdentity=ObjectIdentity
eipDhcp6=_EipDhcp6_ObjectIdentity((1,3,6,1,4,1,2440,1,7))
_EipDhcp6Stat_ObjectIdentity=ObjectIdentity
eipDhcp6Stat=_EipDhcp6Stat_ObjectIdentity((1,3,6,1,4,1,2440,1,7,1))
_EipDhcp6StatTable_Object=MibTable
eipDhcp6StatTable=_EipDhcp6StatTable_Object((1,3,6,1,4,1,2440,1,7,1,1))
if mibBuilder.loadTexts:eipDhcp6StatTable.setStatus(_A)
_EipDhcp6StatEntry_Object=MibTableRow
eipDhcp6StatEntry=_EipDhcp6StatEntry_Object((1,3,6,1,4,1,2440,1,7,1,1,1))
eipDhcp6StatEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:eipDhcp6StatEntry.setStatus(_A)
class _EipDhcp6StatIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDhcp6StatIndex_Type.__name__=_C
_EipDhcp6StatIndex_Object=MibTableColumn
eipDhcp6StatIndex=_EipDhcp6StatIndex_Object((1,3,6,1,4,1,2440,1,7,1,1,1,1),_EipDhcp6StatIndex_Type())
eipDhcp6StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcp6StatIndex.setStatus(_A)
class _EipDhcp6StatName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EipDhcp6StatName_Type.__name__=_C
_EipDhcp6StatName_Object=MibTableColumn
eipDhcp6StatName=_EipDhcp6StatName_Object((1,3,6,1,4,1,2440,1,7,1,1,1,2),_EipDhcp6StatName_Type())
eipDhcp6StatName.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcp6StatName.setStatus(_A)
_EipDhcp6StatValue_Type=Integer32
_EipDhcp6StatValue_Object=MibTableColumn
eipDhcp6StatValue=_EipDhcp6StatValue_Object((1,3,6,1,4,1,2440,1,7,1,1,1,3),_EipDhcp6StatValue_Type())
eipDhcp6StatValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eipDhcp6StatValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eip':eip,'products':products,'eipDhcp':eipDhcp,'eipDhcpStat':eipDhcpStat,'eipDhcpStatTable':eipDhcpStatTable,'eipDhcpStatEntry':eipDhcpStatEntry,'eipDhcpStatIndex':eipDhcpStatIndex,_F:eipDhcpStatName,'eipDhcpStatValue':eipDhcpStatValue,'eipDns':eipDns,'eipDnsStat':eipDnsStat,'eipDnsStatTable':eipDnsStatTable,'eipDnsStatEntry':eipDnsStatEntry,'eipDnsStatIndex':eipDnsStatIndex,_G:eipDnsStatName,'eipDnsStatValue':eipDnsStatValue,'eipDhcp6':eipDhcp6,'eipDhcp6Stat':eipDhcp6Stat,'eipDhcp6StatTable':eipDhcp6StatTable,'eipDhcp6StatEntry':eipDhcp6StatEntry,'eipDhcp6StatIndex':eipDhcp6StatIndex,_H:eipDhcp6StatName,'eipDhcp6StatValue':eipDhcp6StatValue})