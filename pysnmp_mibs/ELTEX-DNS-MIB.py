_I='eltexDnsServerAnswer'
_H='not-accessible'
_G='eltexDnsServerQueryType'
_F='eltexDnsServerQueryQuestion'
_E='read-write'
_D='Integer32'
_C='ELTEX-DNS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltexDnsMIB=ModuleIdentity((1,3,6,1,4,1,35265,46))
if mibBuilder.loadTexts:eltexDnsMIB.setRevisions(('2018-01-14 00:00',))
_EltexDnsObjects_ObjectIdentity=ObjectIdentity
eltexDnsObjects=_EltexDnsObjects_ObjectIdentity((1,3,6,1,4,1,35265,46,1))
_EltexDnsServer_ObjectIdentity=ObjectIdentity
eltexDnsServer=_EltexDnsServer_ObjectIdentity((1,3,6,1,4,1,35265,46,1,1))
_EltexDnsServerGlobals_ObjectIdentity=ObjectIdentity
eltexDnsServerGlobals=_EltexDnsServerGlobals_ObjectIdentity((1,3,6,1,4,1,35265,46,1,1,1))
_EltexDnsServerEnable_Type=TruthValue
_EltexDnsServerEnable_Object=MibScalar
eltexDnsServerEnable=_EltexDnsServerEnable_Object((1,3,6,1,4,1,35265,46,1,1,1,1),_EltexDnsServerEnable_Type())
eltexDnsServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexDnsServerEnable.setStatus(_A)
_EltexDnsServerClearCache_Type=TruthValue
_EltexDnsServerClearCache_Object=MibScalar
eltexDnsServerClearCache=_EltexDnsServerClearCache_Object((1,3,6,1,4,1,35265,46,1,1,1,2),_EltexDnsServerClearCache_Type())
eltexDnsServerClearCache.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexDnsServerClearCache.setStatus(_A)
_EltexDnsServerClearCounters_Type=TruthValue
_EltexDnsServerClearCounters_Object=MibScalar
eltexDnsServerClearCounters=_EltexDnsServerClearCounters_Object((1,3,6,1,4,1,35265,46,1,1,1,3),_EltexDnsServerClearCounters_Type())
eltexDnsServerClearCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexDnsServerClearCounters.setStatus(_A)
_EltexDnsServerCounters_ObjectIdentity=ObjectIdentity
eltexDnsServerCounters=_EltexDnsServerCounters_ObjectIdentity((1,3,6,1,4,1,35265,46,1,1,2))
_EltexDnsServerQueriesCounter_Type=Counter32
_EltexDnsServerQueriesCounter_Object=MibScalar
eltexDnsServerQueriesCounter=_EltexDnsServerQueriesCounter_Object((1,3,6,1,4,1,35265,46,1,1,2,1),_EltexDnsServerQueriesCounter_Type())
eltexDnsServerQueriesCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerQueriesCounter.setStatus(_A)
_EltexDnsServerPendingQueriesCounter_Type=Counter32
_EltexDnsServerPendingQueriesCounter_Object=MibScalar
eltexDnsServerPendingQueriesCounter=_EltexDnsServerPendingQueriesCounter_Object((1,3,6,1,4,1,35265,46,1,1,2,2),_EltexDnsServerPendingQueriesCounter_Type())
eltexDnsServerPendingQueriesCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerPendingQueriesCounter.setStatus(_A)
_EltexDnsServerCacheResponsesCounter_Type=Counter32
_EltexDnsServerCacheResponsesCounter_Object=MibScalar
eltexDnsServerCacheResponsesCounter=_EltexDnsServerCacheResponsesCounter_Object((1,3,6,1,4,1,35265,46,1,1,2,3),_EltexDnsServerCacheResponsesCounter_Type())
eltexDnsServerCacheResponsesCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerCacheResponsesCounter.setStatus(_A)
_EltexDnsServerCacheHitCounter_Type=Counter32
_EltexDnsServerCacheHitCounter_Object=MibScalar
eltexDnsServerCacheHitCounter=_EltexDnsServerCacheHitCounter_Object((1,3,6,1,4,1,35265,46,1,1,2,4),_EltexDnsServerCacheHitCounter_Type())
eltexDnsServerCacheHitCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerCacheHitCounter.setStatus(_A)
_EltexDnsServerCache_ObjectIdentity=ObjectIdentity
eltexDnsServerCache=_EltexDnsServerCache_ObjectIdentity((1,3,6,1,4,1,35265,46,1,1,3))
_EltexDnsServerQueryTable_Object=MibTable
eltexDnsServerQueryTable=_EltexDnsServerQueryTable_Object((1,3,6,1,4,1,35265,46,1,1,3,1))
if mibBuilder.loadTexts:eltexDnsServerQueryTable.setStatus(_A)
_EltexDnsServerQueryEntry_Object=MibTableRow
eltexDnsServerQueryEntry=_EltexDnsServerQueryEntry_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1))
eltexDnsServerQueryEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:eltexDnsServerQueryEntry.setStatus(_A)
_EltexDnsServerQueryQuestion_Type=OctetString
_EltexDnsServerQueryQuestion_Object=MibTableColumn
eltexDnsServerQueryQuestion=_EltexDnsServerQueryQuestion_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1,1),_EltexDnsServerQueryQuestion_Type())
eltexDnsServerQueryQuestion.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexDnsServerQueryQuestion.setStatus(_A)
class _EltexDnsServerQueryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexDnsServerQueryType_Type.__name__=_D
_EltexDnsServerQueryType_Object=MibTableColumn
eltexDnsServerQueryType=_EltexDnsServerQueryType_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1,2),_EltexDnsServerQueryType_Type())
eltexDnsServerQueryType.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexDnsServerQueryType.setStatus(_A)
_EltexDnsServerQueryRemainingTTL_Type=Integer32
_EltexDnsServerQueryRemainingTTL_Object=MibTableColumn
eltexDnsServerQueryRemainingTTL=_EltexDnsServerQueryRemainingTTL_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1,3),_EltexDnsServerQueryRemainingTTL_Type())
eltexDnsServerQueryRemainingTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerQueryRemainingTTL.setStatus(_A)
_EltexDnsServerQuerySourceInetAddressType_Type=InetAddressType
_EltexDnsServerQuerySourceInetAddressType_Object=MibTableColumn
eltexDnsServerQuerySourceInetAddressType=_EltexDnsServerQuerySourceInetAddressType_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1,4),_EltexDnsServerQuerySourceInetAddressType_Type())
eltexDnsServerQuerySourceInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerQuerySourceInetAddressType.setStatus(_A)
_EltexDnsServerQuerySourceInetAddress_Type=InetAddress
_EltexDnsServerQuerySourceInetAddress_Object=MibTableColumn
eltexDnsServerQuerySourceInetAddress=_EltexDnsServerQuerySourceInetAddress_Object((1,3,6,1,4,1,35265,46,1,1,3,1,1,5),_EltexDnsServerQuerySourceInetAddress_Type())
eltexDnsServerQuerySourceInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerQuerySourceInetAddress.setStatus(_A)
_EltexDnsServerAnswerTable_Object=MibTable
eltexDnsServerAnswerTable=_EltexDnsServerAnswerTable_Object((1,3,6,1,4,1,35265,46,1,1,3,2))
if mibBuilder.loadTexts:eltexDnsServerAnswerTable.setStatus(_A)
_EltexDnsServerAnswerEntry_Object=MibTableRow
eltexDnsServerAnswerEntry=_EltexDnsServerAnswerEntry_Object((1,3,6,1,4,1,35265,46,1,1,3,2,1))
eltexDnsServerAnswerEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_I))
if mibBuilder.loadTexts:eltexDnsServerAnswerEntry.setStatus(_A)
_EltexDnsServerAnswer_Type=OctetString
_EltexDnsServerAnswer_Object=MibTableColumn
eltexDnsServerAnswer=_EltexDnsServerAnswer_Object((1,3,6,1,4,1,35265,46,1,1,3,2,1,1),_EltexDnsServerAnswer_Type())
eltexDnsServerAnswer.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexDnsServerAnswer.setStatus(_A)
class _EltexDnsServerAnswerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexDnsServerAnswerType_Type.__name__=_D
_EltexDnsServerAnswerType_Object=MibTableColumn
eltexDnsServerAnswerType=_EltexDnsServerAnswerType_Object((1,3,6,1,4,1,35265,46,1,1,3,2,1,2),_EltexDnsServerAnswerType_Type())
eltexDnsServerAnswerType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerAnswerType.setStatus(_A)
_EltexDnsServerAnswerTTL_Type=Integer32
_EltexDnsServerAnswerTTL_Object=MibTableColumn
eltexDnsServerAnswerTTL=_EltexDnsServerAnswerTTL_Object((1,3,6,1,4,1,35265,46,1,1,3,2,1,3),_EltexDnsServerAnswerTTL_Type())
eltexDnsServerAnswerTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexDnsServerAnswerTTL.setStatus(_A)
_EltexDnsClient_ObjectIdentity=ObjectIdentity
eltexDnsClient=_EltexDnsClient_ObjectIdentity((1,3,6,1,4,1,35265,46,1,2))
mibBuilder.exportSymbols(_C,**{'eltexDnsMIB':eltexDnsMIB,'eltexDnsObjects':eltexDnsObjects,'eltexDnsServer':eltexDnsServer,'eltexDnsServerGlobals':eltexDnsServerGlobals,'eltexDnsServerEnable':eltexDnsServerEnable,'eltexDnsServerClearCache':eltexDnsServerClearCache,'eltexDnsServerClearCounters':eltexDnsServerClearCounters,'eltexDnsServerCounters':eltexDnsServerCounters,'eltexDnsServerQueriesCounter':eltexDnsServerQueriesCounter,'eltexDnsServerPendingQueriesCounter':eltexDnsServerPendingQueriesCounter,'eltexDnsServerCacheResponsesCounter':eltexDnsServerCacheResponsesCounter,'eltexDnsServerCacheHitCounter':eltexDnsServerCacheHitCounter,'eltexDnsServerCache':eltexDnsServerCache,'eltexDnsServerQueryTable':eltexDnsServerQueryTable,'eltexDnsServerQueryEntry':eltexDnsServerQueryEntry,_F:eltexDnsServerQueryQuestion,_G:eltexDnsServerQueryType,'eltexDnsServerQueryRemainingTTL':eltexDnsServerQueryRemainingTTL,'eltexDnsServerQuerySourceInetAddressType':eltexDnsServerQuerySourceInetAddressType,'eltexDnsServerQuerySourceInetAddress':eltexDnsServerQuerySourceInetAddress,'eltexDnsServerAnswerTable':eltexDnsServerAnswerTable,'eltexDnsServerAnswerEntry':eltexDnsServerAnswerEntry,_I:eltexDnsServerAnswer,'eltexDnsServerAnswerType':eltexDnsServerAnswerType,'eltexDnsServerAnswerTTL':eltexDnsServerAnswerTTL,'eltexDnsClient':eltexDnsClient})