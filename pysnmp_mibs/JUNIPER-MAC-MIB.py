_H='not-accessible'
_G='jnxSourceMacAddress'
_F='jnxVlanIndex'
_E='ifIndex'
_D='IF-MIB'
_C='JUNIPER-MAC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
jnxMac=ModuleIdentity((1,3,6,1,4,1,2636,3,23))
if mibBuilder.loadTexts:jnxMac.setRevisions(('2002-10-10 00:00',))
class JnxVlanIndex(TextualConvention,Unsigned32):status=_A
_JnxMacStats_ObjectIdentity=ObjectIdentity
jnxMacStats=_JnxMacStats_ObjectIdentity((1,3,6,1,4,1,2636,3,23,1))
_JnxMacStatsTable_Object=MibTable
jnxMacStatsTable=_JnxMacStatsTable_Object((1,3,6,1,4,1,2636,3,23,1,1))
if mibBuilder.loadTexts:jnxMacStatsTable.setStatus(_A)
_JnxMacStatsEntry_Object=MibTableRow
jnxMacStatsEntry=_JnxMacStatsEntry_Object((1,3,6,1,4,1,2636,3,23,1,1,1))
jnxMacStatsEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:jnxMacStatsEntry.setStatus(_A)
_JnxVlanIndex_Type=JnxVlanIndex
_JnxVlanIndex_Object=MibTableColumn
jnxVlanIndex=_JnxVlanIndex_Object((1,3,6,1,4,1,2636,3,23,1,1,1,1),_JnxVlanIndex_Type())
jnxVlanIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxVlanIndex.setStatus(_A)
_JnxSourceMacAddress_Type=MacAddress
_JnxSourceMacAddress_Object=MibTableColumn
jnxSourceMacAddress=_JnxSourceMacAddress_Object((1,3,6,1,4,1,2636,3,23,1,1,1,2),_JnxSourceMacAddress_Type())
jnxSourceMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxSourceMacAddress.setStatus(_A)
_JnxMacHCInOctets_Type=Counter64
_JnxMacHCInOctets_Object=MibTableColumn
jnxMacHCInOctets=_JnxMacHCInOctets_Object((1,3,6,1,4,1,2636,3,23,1,1,1,3),_JnxMacHCInOctets_Type())
jnxMacHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxMacHCInOctets.setStatus(_A)
_JnxMacHCInFrames_Type=Counter64
_JnxMacHCInFrames_Object=MibTableColumn
jnxMacHCInFrames=_JnxMacHCInFrames_Object((1,3,6,1,4,1,2636,3,23,1,1,1,4),_JnxMacHCInFrames_Type())
jnxMacHCInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxMacHCInFrames.setStatus(_A)
_JnxMacHCOutOctets_Type=Counter64
_JnxMacHCOutOctets_Object=MibTableColumn
jnxMacHCOutOctets=_JnxMacHCOutOctets_Object((1,3,6,1,4,1,2636,3,23,1,1,1,5),_JnxMacHCOutOctets_Type())
jnxMacHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxMacHCOutOctets.setStatus(_A)
_JnxMacHCOutFrames_Type=Counter64
_JnxMacHCOutFrames_Object=MibTableColumn
jnxMacHCOutFrames=_JnxMacHCOutFrames_Object((1,3,6,1,4,1,2636,3,23,1,1,1,6),_JnxMacHCOutFrames_Type())
jnxMacHCOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxMacHCOutFrames.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'JnxVlanIndex':JnxVlanIndex,'jnxMac':jnxMac,'jnxMacStats':jnxMacStats,'jnxMacStatsTable':jnxMacStatsTable,'jnxMacStatsEntry':jnxMacStatsEntry,_F:jnxVlanIndex,_G:jnxSourceMacAddress,'jnxMacHCInOctets':jnxMacHCInOctets,'jnxMacHCInFrames':jnxMacHCInFrames,'jnxMacHCOutOctets':jnxMacHCOutOctets,'jnxMacHCOutFrames':jnxMacHCOutFrames})