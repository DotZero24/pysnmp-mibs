_H='ipfAccOutIndex'
_G='ipfAccInIndex'
_F='ipfOutIndex'
_E='ipfInIndex'
_D='UCD-IPFILTER-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ucdExperimental,=mibBuilder.importSymbols('UCD-SNMP-MIB','ucdExperimental')
ucdIpFilter=ModuleIdentity((1,3,6,1,4,1,2021,13,2))
if mibBuilder.loadTexts:ucdIpFilter.setRevisions(('2000-01-26 00:00','1999-12-15 00:00'))
_IpfInTable_Object=MibTable
ipfInTable=_IpfInTable_Object((1,3,6,1,4,1,2021,13,2,1))
if mibBuilder.loadTexts:ipfInTable.setStatus(_A)
_IpfInEntry_Object=MibTableRow
ipfInEntry=_IpfInEntry_Object((1,3,6,1,4,1,2021,13,2,1,1))
ipfInEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ipfInEntry.setStatus(_A)
class _IpfInIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpfInIndex_Type.__name__=_C
_IpfInIndex_Object=MibTableColumn
ipfInIndex=_IpfInIndex_Object((1,3,6,1,4,1,2021,13,2,1,1,1),_IpfInIndex_Type())
ipfInIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfInIndex.setStatus(_A)
_IpfInRule_Type=OctetString
_IpfInRule_Object=MibTableColumn
ipfInRule=_IpfInRule_Object((1,3,6,1,4,1,2021,13,2,1,1,2),_IpfInRule_Type())
ipfInRule.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfInRule.setStatus(_A)
_IpfInHits_Type=Counter32
_IpfInHits_Object=MibTableColumn
ipfInHits=_IpfInHits_Object((1,3,6,1,4,1,2021,13,2,1,1,3),_IpfInHits_Type())
ipfInHits.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfInHits.setStatus(_A)
_IpfOutTable_Object=MibTable
ipfOutTable=_IpfOutTable_Object((1,3,6,1,4,1,2021,13,2,2))
if mibBuilder.loadTexts:ipfOutTable.setStatus(_A)
_IpfOutEntry_Object=MibTableRow
ipfOutEntry=_IpfOutEntry_Object((1,3,6,1,4,1,2021,13,2,2,1))
ipfOutEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ipfOutEntry.setStatus(_A)
class _IpfOutIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpfOutIndex_Type.__name__=_C
_IpfOutIndex_Object=MibTableColumn
ipfOutIndex=_IpfOutIndex_Object((1,3,6,1,4,1,2021,13,2,2,1,1),_IpfOutIndex_Type())
ipfOutIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfOutIndex.setStatus(_A)
_IpfOutRule_Type=OctetString
_IpfOutRule_Object=MibTableColumn
ipfOutRule=_IpfOutRule_Object((1,3,6,1,4,1,2021,13,2,2,1,2),_IpfOutRule_Type())
ipfOutRule.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfOutRule.setStatus(_A)
_IpfOutHits_Type=Counter32
_IpfOutHits_Object=MibTableColumn
ipfOutHits=_IpfOutHits_Object((1,3,6,1,4,1,2021,13,2,2,1,3),_IpfOutHits_Type())
ipfOutHits.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfOutHits.setStatus(_A)
_IpfAccInTable_Object=MibTable
ipfAccInTable=_IpfAccInTable_Object((1,3,6,1,4,1,2021,13,2,3))
if mibBuilder.loadTexts:ipfAccInTable.setStatus(_A)
_IpfAccInEntry_Object=MibTableRow
ipfAccInEntry=_IpfAccInEntry_Object((1,3,6,1,4,1,2021,13,2,3,1))
ipfAccInEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:ipfAccInEntry.setStatus(_A)
class _IpfAccInIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpfAccInIndex_Type.__name__=_C
_IpfAccInIndex_Object=MibTableColumn
ipfAccInIndex=_IpfAccInIndex_Object((1,3,6,1,4,1,2021,13,2,3,1,1),_IpfAccInIndex_Type())
ipfAccInIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccInIndex.setStatus(_A)
_IpfAccInRule_Type=OctetString
_IpfAccInRule_Object=MibTableColumn
ipfAccInRule=_IpfAccInRule_Object((1,3,6,1,4,1,2021,13,2,3,1,2),_IpfAccInRule_Type())
ipfAccInRule.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccInRule.setStatus(_A)
_IpfAccInHits_Type=Counter32
_IpfAccInHits_Object=MibTableColumn
ipfAccInHits=_IpfAccInHits_Object((1,3,6,1,4,1,2021,13,2,3,1,3),_IpfAccInHits_Type())
ipfAccInHits.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccInHits.setStatus(_A)
_IpfAccInBytes_Type=Counter32
_IpfAccInBytes_Object=MibTableColumn
ipfAccInBytes=_IpfAccInBytes_Object((1,3,6,1,4,1,2021,13,2,3,1,4),_IpfAccInBytes_Type())
ipfAccInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccInBytes.setStatus(_A)
_IpfAccOutTable_Object=MibTable
ipfAccOutTable=_IpfAccOutTable_Object((1,3,6,1,4,1,2021,13,2,4))
if mibBuilder.loadTexts:ipfAccOutTable.setStatus(_A)
_IpfAccOutEntry_Object=MibTableRow
ipfAccOutEntry=_IpfAccOutEntry_Object((1,3,6,1,4,1,2021,13,2,4,1))
ipfAccOutEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:ipfAccOutEntry.setStatus(_A)
class _IpfAccOutIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpfAccOutIndex_Type.__name__=_C
_IpfAccOutIndex_Object=MibTableColumn
ipfAccOutIndex=_IpfAccOutIndex_Object((1,3,6,1,4,1,2021,13,2,4,1,1),_IpfAccOutIndex_Type())
ipfAccOutIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccOutIndex.setStatus(_A)
_IpfAccOutRule_Type=OctetString
_IpfAccOutRule_Object=MibTableColumn
ipfAccOutRule=_IpfAccOutRule_Object((1,3,6,1,4,1,2021,13,2,4,1,2),_IpfAccOutRule_Type())
ipfAccOutRule.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccOutRule.setStatus(_A)
_IpfAccOutHits_Type=Counter32
_IpfAccOutHits_Object=MibTableColumn
ipfAccOutHits=_IpfAccOutHits_Object((1,3,6,1,4,1,2021,13,2,4,1,3),_IpfAccOutHits_Type())
ipfAccOutHits.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccOutHits.setStatus(_A)
_IpfAccOutBytes_Type=Counter32
_IpfAccOutBytes_Object=MibTableColumn
ipfAccOutBytes=_IpfAccOutBytes_Object((1,3,6,1,4,1,2021,13,2,4,1,4),_IpfAccOutBytes_Type())
ipfAccOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ipfAccOutBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ucdIpFilter':ucdIpFilter,'ipfInTable':ipfInTable,'ipfInEntry':ipfInEntry,_E:ipfInIndex,'ipfInRule':ipfInRule,'ipfInHits':ipfInHits,'ipfOutTable':ipfOutTable,'ipfOutEntry':ipfOutEntry,_F:ipfOutIndex,'ipfOutRule':ipfOutRule,'ipfOutHits':ipfOutHits,'ipfAccInTable':ipfAccInTable,'ipfAccInEntry':ipfAccInEntry,_G:ipfAccInIndex,'ipfAccInRule':ipfAccInRule,'ipfAccInHits':ipfAccInHits,'ipfAccInBytes':ipfAccInBytes,'ipfAccOutTable':ipfAccOutTable,'ipfAccOutEntry':ipfAccOutEntry,_H:ipfAccOutIndex,'ipfAccOutRule':ipfAccOutRule,'ipfAccOutHits':ipfAccOutHits,'ipfAccOutBytes':ipfAccOutBytes})