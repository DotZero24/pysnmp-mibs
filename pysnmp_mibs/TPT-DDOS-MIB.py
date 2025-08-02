_A0='acceptEstHistDaysIndex'
_z='acceptEstHistDaysGlobalID'
_y='acceptEstHistHoursIndex'
_x='acceptEstHistHoursGlobalID'
_w='acceptEstHistMinutesIndex'
_v='acceptEstHistMinutesGlobalID'
_u='acceptEstHistSecondsIndex'
_t='acceptEstHistSecondsGlobalID'
_s='rejectEstHistDaysIndex'
_r='rejectEstHistDaysGlobalID'
_q='rejectEstHistHoursIndex'
_p='rejectEstHistHoursGlobalID'
_o='rejectEstHistMinutesIndex'
_n='rejectEstHistMinutesGlobalID'
_m='rejectEstHistSecondsIndex'
_l='rejectEstHistSecondsGlobalID'
_k='acceptCpsHistDaysIndex'
_j='acceptCpsHistDaysGlobalID'
_i='acceptCpsHistHoursIndex'
_h='acceptCpsHistHoursGlobalID'
_g='acceptCpsHistMinutesIndex'
_f='acceptCpsHistMinutesGlobalID'
_e='acceptCpsHistSecondsIndex'
_d='acceptCpsHistSecondsGlobalID'
_c='rejectCpsHistDaysIndex'
_b='rejectCpsHistDaysGlobalID'
_a='rejectCpsHistHoursIndex'
_Z='rejectCpsHistHoursGlobalID'
_Y='rejectCpsHistMinutesIndex'
_X='rejectCpsHistMinutesGlobalID'
_W='rejectCpsHistSecondsIndex'
_V='rejectCpsHistSecondsGlobalID'
_U='proxyConnHistDaysIndex'
_T='proxyConnHistDaysGlobalID'
_S='proxyConnHistHoursIndex'
_R='proxyConnHistHoursGlobalID'
_Q='proxyConnHistMinutesIndex'
_P='proxyConnHistMinutesGlobalID'
_O='proxyConnHistSecondsIndex'
_N='proxyConnHistSecondsGlobalID'
_M='rejectSynHistDaysIndex'
_L='rejectSynHistDaysGlobalID'
_K='rejectSynHistHoursIndex'
_J='rejectSynHistHoursGlobalID'
_I='rejectSynHistMinutesIndex'
_H='rejectSynHistMinutesGlobalID'
_G='rejectSynHistSecondsIndex'
_F='rejectSynHistSecondsGlobalID'
_E='OctetString'
_D='read-only'
_C='not-accessible'
_B='TPT-DDOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_ddos=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,9))
if mibBuilder.loadTexts:tpt_ddos.setRevisions(('2016-05-25 18:54',))
_RejectSynHistSecondsTable_Object=MibTable
rejectSynHistSecondsTable=_RejectSynHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,5))
if mibBuilder.loadTexts:rejectSynHistSecondsTable.setStatus(_A)
_RejectSynHistSecondsEntry_Object=MibTableRow
rejectSynHistSecondsEntry=_RejectSynHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,5,1))
rejectSynHistSecondsEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:rejectSynHistSecondsEntry.setStatus(_A)
class _RejectSynHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectSynHistSecondsGlobalID_Type.__name__=_E
_RejectSynHistSecondsGlobalID_Object=MibTableColumn
rejectSynHistSecondsGlobalID=_RejectSynHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,5,1,1),_RejectSynHistSecondsGlobalID_Type())
rejectSynHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistSecondsGlobalID.setStatus(_A)
_RejectSynHistSecondsIndex_Type=Unsigned32
_RejectSynHistSecondsIndex_Object=MibTableColumn
rejectSynHistSecondsIndex=_RejectSynHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,5,1,2),_RejectSynHistSecondsIndex_Type())
rejectSynHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistSecondsIndex.setStatus(_A)
_RejectSynHistSecondsUnitCount_Type=Counter64
_RejectSynHistSecondsUnitCount_Object=MibTableColumn
rejectSynHistSecondsUnitCount=_RejectSynHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,5,1,3),_RejectSynHistSecondsUnitCount_Type())
rejectSynHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistSecondsUnitCount.setStatus(_A)
_RejectSynHistSecondsTimestamp_Type=Unsigned32
_RejectSynHistSecondsTimestamp_Object=MibTableColumn
rejectSynHistSecondsTimestamp=_RejectSynHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,5,1,4),_RejectSynHistSecondsTimestamp_Type())
rejectSynHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistSecondsTimestamp.setStatus(_A)
_RejectSynHistMinutesTable_Object=MibTable
rejectSynHistMinutesTable=_RejectSynHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,6))
if mibBuilder.loadTexts:rejectSynHistMinutesTable.setStatus(_A)
_RejectSynHistMinutesEntry_Object=MibTableRow
rejectSynHistMinutesEntry=_RejectSynHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,6,1))
rejectSynHistMinutesEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:rejectSynHistMinutesEntry.setStatus(_A)
class _RejectSynHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectSynHistMinutesGlobalID_Type.__name__=_E
_RejectSynHistMinutesGlobalID_Object=MibTableColumn
rejectSynHistMinutesGlobalID=_RejectSynHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,6,1,1),_RejectSynHistMinutesGlobalID_Type())
rejectSynHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistMinutesGlobalID.setStatus(_A)
_RejectSynHistMinutesIndex_Type=Unsigned32
_RejectSynHistMinutesIndex_Object=MibTableColumn
rejectSynHistMinutesIndex=_RejectSynHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,6,1,2),_RejectSynHistMinutesIndex_Type())
rejectSynHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistMinutesIndex.setStatus(_A)
_RejectSynHistMinutesUnitCount_Type=Counter64
_RejectSynHistMinutesUnitCount_Object=MibTableColumn
rejectSynHistMinutesUnitCount=_RejectSynHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,6,1,3),_RejectSynHistMinutesUnitCount_Type())
rejectSynHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistMinutesUnitCount.setStatus(_A)
_RejectSynHistMinutesTimestamp_Type=Unsigned32
_RejectSynHistMinutesTimestamp_Object=MibTableColumn
rejectSynHistMinutesTimestamp=_RejectSynHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,6,1,4),_RejectSynHistMinutesTimestamp_Type())
rejectSynHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistMinutesTimestamp.setStatus(_A)
_RejectSynHistHoursTable_Object=MibTable
rejectSynHistHoursTable=_RejectSynHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,7))
if mibBuilder.loadTexts:rejectSynHistHoursTable.setStatus(_A)
_RejectSynHistHoursEntry_Object=MibTableRow
rejectSynHistHoursEntry=_RejectSynHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,7,1))
rejectSynHistHoursEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:rejectSynHistHoursEntry.setStatus(_A)
class _RejectSynHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectSynHistHoursGlobalID_Type.__name__=_E
_RejectSynHistHoursGlobalID_Object=MibTableColumn
rejectSynHistHoursGlobalID=_RejectSynHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,7,1,1),_RejectSynHistHoursGlobalID_Type())
rejectSynHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistHoursGlobalID.setStatus(_A)
_RejectSynHistHoursIndex_Type=Unsigned32
_RejectSynHistHoursIndex_Object=MibTableColumn
rejectSynHistHoursIndex=_RejectSynHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,7,1,2),_RejectSynHistHoursIndex_Type())
rejectSynHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistHoursIndex.setStatus(_A)
_RejectSynHistHoursUnitCount_Type=Counter64
_RejectSynHistHoursUnitCount_Object=MibTableColumn
rejectSynHistHoursUnitCount=_RejectSynHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,7,1,3),_RejectSynHistHoursUnitCount_Type())
rejectSynHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistHoursUnitCount.setStatus(_A)
_RejectSynHistHoursTimestamp_Type=Unsigned32
_RejectSynHistHoursTimestamp_Object=MibTableColumn
rejectSynHistHoursTimestamp=_RejectSynHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,7,1,4),_RejectSynHistHoursTimestamp_Type())
rejectSynHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistHoursTimestamp.setStatus(_A)
_RejectSynHistDaysTable_Object=MibTable
rejectSynHistDaysTable=_RejectSynHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,8))
if mibBuilder.loadTexts:rejectSynHistDaysTable.setStatus(_A)
_RejectSynHistDaysEntry_Object=MibTableRow
rejectSynHistDaysEntry=_RejectSynHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,8,1))
rejectSynHistDaysEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rejectSynHistDaysEntry.setStatus(_A)
class _RejectSynHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectSynHistDaysGlobalID_Type.__name__=_E
_RejectSynHistDaysGlobalID_Object=MibTableColumn
rejectSynHistDaysGlobalID=_RejectSynHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,8,1,1),_RejectSynHistDaysGlobalID_Type())
rejectSynHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistDaysGlobalID.setStatus(_A)
_RejectSynHistDaysIndex_Type=Unsigned32
_RejectSynHistDaysIndex_Object=MibTableColumn
rejectSynHistDaysIndex=_RejectSynHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,8,1,2),_RejectSynHistDaysIndex_Type())
rejectSynHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectSynHistDaysIndex.setStatus(_A)
_RejectSynHistDaysUnitCount_Type=Counter64
_RejectSynHistDaysUnitCount_Object=MibTableColumn
rejectSynHistDaysUnitCount=_RejectSynHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,8,1,3),_RejectSynHistDaysUnitCount_Type())
rejectSynHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistDaysUnitCount.setStatus(_A)
_RejectSynHistDaysTimestamp_Type=Unsigned32
_RejectSynHistDaysTimestamp_Object=MibTableColumn
rejectSynHistDaysTimestamp=_RejectSynHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,8,1,4),_RejectSynHistDaysTimestamp_Type())
rejectSynHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectSynHistDaysTimestamp.setStatus(_A)
_ProxyConnHistSecondsTable_Object=MibTable
proxyConnHistSecondsTable=_ProxyConnHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,9))
if mibBuilder.loadTexts:proxyConnHistSecondsTable.setStatus(_A)
_ProxyConnHistSecondsEntry_Object=MibTableRow
proxyConnHistSecondsEntry=_ProxyConnHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,9,1))
proxyConnHistSecondsEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:proxyConnHistSecondsEntry.setStatus(_A)
class _ProxyConnHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ProxyConnHistSecondsGlobalID_Type.__name__=_E
_ProxyConnHistSecondsGlobalID_Object=MibTableColumn
proxyConnHistSecondsGlobalID=_ProxyConnHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,9,1,1),_ProxyConnHistSecondsGlobalID_Type())
proxyConnHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistSecondsGlobalID.setStatus(_A)
_ProxyConnHistSecondsIndex_Type=Unsigned32
_ProxyConnHistSecondsIndex_Object=MibTableColumn
proxyConnHistSecondsIndex=_ProxyConnHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,9,1,2),_ProxyConnHistSecondsIndex_Type())
proxyConnHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistSecondsIndex.setStatus(_A)
_ProxyConnHistSecondsUnitCount_Type=Counter64
_ProxyConnHistSecondsUnitCount_Object=MibTableColumn
proxyConnHistSecondsUnitCount=_ProxyConnHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,9,1,3),_ProxyConnHistSecondsUnitCount_Type())
proxyConnHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistSecondsUnitCount.setStatus(_A)
_ProxyConnHistSecondsTimestamp_Type=Unsigned32
_ProxyConnHistSecondsTimestamp_Object=MibTableColumn
proxyConnHistSecondsTimestamp=_ProxyConnHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,9,1,4),_ProxyConnHistSecondsTimestamp_Type())
proxyConnHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistSecondsTimestamp.setStatus(_A)
_ProxyConnHistMinutesTable_Object=MibTable
proxyConnHistMinutesTable=_ProxyConnHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,10))
if mibBuilder.loadTexts:proxyConnHistMinutesTable.setStatus(_A)
_ProxyConnHistMinutesEntry_Object=MibTableRow
proxyConnHistMinutesEntry=_ProxyConnHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,10,1))
proxyConnHistMinutesEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:proxyConnHistMinutesEntry.setStatus(_A)
class _ProxyConnHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ProxyConnHistMinutesGlobalID_Type.__name__=_E
_ProxyConnHistMinutesGlobalID_Object=MibTableColumn
proxyConnHistMinutesGlobalID=_ProxyConnHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,10,1,1),_ProxyConnHistMinutesGlobalID_Type())
proxyConnHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistMinutesGlobalID.setStatus(_A)
_ProxyConnHistMinutesIndex_Type=Unsigned32
_ProxyConnHistMinutesIndex_Object=MibTableColumn
proxyConnHistMinutesIndex=_ProxyConnHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,10,1,2),_ProxyConnHistMinutesIndex_Type())
proxyConnHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistMinutesIndex.setStatus(_A)
_ProxyConnHistMinutesUnitCount_Type=Counter64
_ProxyConnHistMinutesUnitCount_Object=MibTableColumn
proxyConnHistMinutesUnitCount=_ProxyConnHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,10,1,3),_ProxyConnHistMinutesUnitCount_Type())
proxyConnHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistMinutesUnitCount.setStatus(_A)
_ProxyConnHistMinutesTimestamp_Type=Unsigned32
_ProxyConnHistMinutesTimestamp_Object=MibTableColumn
proxyConnHistMinutesTimestamp=_ProxyConnHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,10,1,4),_ProxyConnHistMinutesTimestamp_Type())
proxyConnHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistMinutesTimestamp.setStatus(_A)
_ProxyConnHistHoursTable_Object=MibTable
proxyConnHistHoursTable=_ProxyConnHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,11))
if mibBuilder.loadTexts:proxyConnHistHoursTable.setStatus(_A)
_ProxyConnHistHoursEntry_Object=MibTableRow
proxyConnHistHoursEntry=_ProxyConnHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,11,1))
proxyConnHistHoursEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:proxyConnHistHoursEntry.setStatus(_A)
class _ProxyConnHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ProxyConnHistHoursGlobalID_Type.__name__=_E
_ProxyConnHistHoursGlobalID_Object=MibTableColumn
proxyConnHistHoursGlobalID=_ProxyConnHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,11,1,1),_ProxyConnHistHoursGlobalID_Type())
proxyConnHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistHoursGlobalID.setStatus(_A)
_ProxyConnHistHoursIndex_Type=Unsigned32
_ProxyConnHistHoursIndex_Object=MibTableColumn
proxyConnHistHoursIndex=_ProxyConnHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,11,1,2),_ProxyConnHistHoursIndex_Type())
proxyConnHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistHoursIndex.setStatus(_A)
_ProxyConnHistHoursUnitCount_Type=Counter64
_ProxyConnHistHoursUnitCount_Object=MibTableColumn
proxyConnHistHoursUnitCount=_ProxyConnHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,11,1,3),_ProxyConnHistHoursUnitCount_Type())
proxyConnHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistHoursUnitCount.setStatus(_A)
_ProxyConnHistHoursTimestamp_Type=Unsigned32
_ProxyConnHistHoursTimestamp_Object=MibTableColumn
proxyConnHistHoursTimestamp=_ProxyConnHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,11,1,4),_ProxyConnHistHoursTimestamp_Type())
proxyConnHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistHoursTimestamp.setStatus(_A)
_ProxyConnHistDaysTable_Object=MibTable
proxyConnHistDaysTable=_ProxyConnHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,12))
if mibBuilder.loadTexts:proxyConnHistDaysTable.setStatus(_A)
_ProxyConnHistDaysEntry_Object=MibTableRow
proxyConnHistDaysEntry=_ProxyConnHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,12,1))
proxyConnHistDaysEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:proxyConnHistDaysEntry.setStatus(_A)
class _ProxyConnHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ProxyConnHistDaysGlobalID_Type.__name__=_E
_ProxyConnHistDaysGlobalID_Object=MibTableColumn
proxyConnHistDaysGlobalID=_ProxyConnHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,12,1,1),_ProxyConnHistDaysGlobalID_Type())
proxyConnHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistDaysGlobalID.setStatus(_A)
_ProxyConnHistDaysIndex_Type=Unsigned32
_ProxyConnHistDaysIndex_Object=MibTableColumn
proxyConnHistDaysIndex=_ProxyConnHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,12,1,2),_ProxyConnHistDaysIndex_Type())
proxyConnHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyConnHistDaysIndex.setStatus(_A)
_ProxyConnHistDaysUnitCount_Type=Counter64
_ProxyConnHistDaysUnitCount_Object=MibTableColumn
proxyConnHistDaysUnitCount=_ProxyConnHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,12,1,3),_ProxyConnHistDaysUnitCount_Type())
proxyConnHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistDaysUnitCount.setStatus(_A)
_ProxyConnHistDaysTimestamp_Type=Unsigned32
_ProxyConnHistDaysTimestamp_Object=MibTableColumn
proxyConnHistDaysTimestamp=_ProxyConnHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,12,1,4),_ProxyConnHistDaysTimestamp_Type())
proxyConnHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:proxyConnHistDaysTimestamp.setStatus(_A)
_RejectCpsHistSecondsTable_Object=MibTable
rejectCpsHistSecondsTable=_RejectCpsHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,15))
if mibBuilder.loadTexts:rejectCpsHistSecondsTable.setStatus(_A)
_RejectCpsHistSecondsEntry_Object=MibTableRow
rejectCpsHistSecondsEntry=_RejectCpsHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,15,1))
rejectCpsHistSecondsEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:rejectCpsHistSecondsEntry.setStatus(_A)
class _RejectCpsHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectCpsHistSecondsGlobalID_Type.__name__=_E
_RejectCpsHistSecondsGlobalID_Object=MibTableColumn
rejectCpsHistSecondsGlobalID=_RejectCpsHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,15,1,1),_RejectCpsHistSecondsGlobalID_Type())
rejectCpsHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistSecondsGlobalID.setStatus(_A)
_RejectCpsHistSecondsIndex_Type=Unsigned32
_RejectCpsHistSecondsIndex_Object=MibTableColumn
rejectCpsHistSecondsIndex=_RejectCpsHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,15,1,2),_RejectCpsHistSecondsIndex_Type())
rejectCpsHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistSecondsIndex.setStatus(_A)
_RejectCpsHistSecondsUnitCount_Type=Counter64
_RejectCpsHistSecondsUnitCount_Object=MibTableColumn
rejectCpsHistSecondsUnitCount=_RejectCpsHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,15,1,3),_RejectCpsHistSecondsUnitCount_Type())
rejectCpsHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistSecondsUnitCount.setStatus(_A)
_RejectCpsHistSecondsTimestamp_Type=Unsigned32
_RejectCpsHistSecondsTimestamp_Object=MibTableColumn
rejectCpsHistSecondsTimestamp=_RejectCpsHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,15,1,4),_RejectCpsHistSecondsTimestamp_Type())
rejectCpsHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistSecondsTimestamp.setStatus(_A)
_RejectCpsHistMinutesTable_Object=MibTable
rejectCpsHistMinutesTable=_RejectCpsHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,16))
if mibBuilder.loadTexts:rejectCpsHistMinutesTable.setStatus(_A)
_RejectCpsHistMinutesEntry_Object=MibTableRow
rejectCpsHistMinutesEntry=_RejectCpsHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,16,1))
rejectCpsHistMinutesEntry.setIndexNames((0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:rejectCpsHistMinutesEntry.setStatus(_A)
class _RejectCpsHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectCpsHistMinutesGlobalID_Type.__name__=_E
_RejectCpsHistMinutesGlobalID_Object=MibTableColumn
rejectCpsHistMinutesGlobalID=_RejectCpsHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,16,1,1),_RejectCpsHistMinutesGlobalID_Type())
rejectCpsHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistMinutesGlobalID.setStatus(_A)
_RejectCpsHistMinutesIndex_Type=Unsigned32
_RejectCpsHistMinutesIndex_Object=MibTableColumn
rejectCpsHistMinutesIndex=_RejectCpsHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,16,1,2),_RejectCpsHistMinutesIndex_Type())
rejectCpsHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistMinutesIndex.setStatus(_A)
_RejectCpsHistMinutesUnitCount_Type=Counter64
_RejectCpsHistMinutesUnitCount_Object=MibTableColumn
rejectCpsHistMinutesUnitCount=_RejectCpsHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,16,1,3),_RejectCpsHistMinutesUnitCount_Type())
rejectCpsHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistMinutesUnitCount.setStatus(_A)
_RejectCpsHistMinutesTimestamp_Type=Unsigned32
_RejectCpsHistMinutesTimestamp_Object=MibTableColumn
rejectCpsHistMinutesTimestamp=_RejectCpsHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,16,1,4),_RejectCpsHistMinutesTimestamp_Type())
rejectCpsHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistMinutesTimestamp.setStatus(_A)
_RejectCpsHistHoursTable_Object=MibTable
rejectCpsHistHoursTable=_RejectCpsHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,17))
if mibBuilder.loadTexts:rejectCpsHistHoursTable.setStatus(_A)
_RejectCpsHistHoursEntry_Object=MibTableRow
rejectCpsHistHoursEntry=_RejectCpsHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,17,1))
rejectCpsHistHoursEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:rejectCpsHistHoursEntry.setStatus(_A)
class _RejectCpsHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectCpsHistHoursGlobalID_Type.__name__=_E
_RejectCpsHistHoursGlobalID_Object=MibTableColumn
rejectCpsHistHoursGlobalID=_RejectCpsHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,17,1,1),_RejectCpsHistHoursGlobalID_Type())
rejectCpsHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistHoursGlobalID.setStatus(_A)
_RejectCpsHistHoursIndex_Type=Unsigned32
_RejectCpsHistHoursIndex_Object=MibTableColumn
rejectCpsHistHoursIndex=_RejectCpsHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,17,1,2),_RejectCpsHistHoursIndex_Type())
rejectCpsHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistHoursIndex.setStatus(_A)
_RejectCpsHistHoursUnitCount_Type=Counter64
_RejectCpsHistHoursUnitCount_Object=MibTableColumn
rejectCpsHistHoursUnitCount=_RejectCpsHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,17,1,3),_RejectCpsHistHoursUnitCount_Type())
rejectCpsHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistHoursUnitCount.setStatus(_A)
_RejectCpsHistHoursTimestamp_Type=Unsigned32
_RejectCpsHistHoursTimestamp_Object=MibTableColumn
rejectCpsHistHoursTimestamp=_RejectCpsHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,17,1,4),_RejectCpsHistHoursTimestamp_Type())
rejectCpsHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistHoursTimestamp.setStatus(_A)
_RejectCpsHistDaysTable_Object=MibTable
rejectCpsHistDaysTable=_RejectCpsHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,18))
if mibBuilder.loadTexts:rejectCpsHistDaysTable.setStatus(_A)
_RejectCpsHistDaysEntry_Object=MibTableRow
rejectCpsHistDaysEntry=_RejectCpsHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,18,1))
rejectCpsHistDaysEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:rejectCpsHistDaysEntry.setStatus(_A)
class _RejectCpsHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectCpsHistDaysGlobalID_Type.__name__=_E
_RejectCpsHistDaysGlobalID_Object=MibTableColumn
rejectCpsHistDaysGlobalID=_RejectCpsHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,18,1,1),_RejectCpsHistDaysGlobalID_Type())
rejectCpsHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistDaysGlobalID.setStatus(_A)
_RejectCpsHistDaysIndex_Type=Unsigned32
_RejectCpsHistDaysIndex_Object=MibTableColumn
rejectCpsHistDaysIndex=_RejectCpsHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,18,1,2),_RejectCpsHistDaysIndex_Type())
rejectCpsHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectCpsHistDaysIndex.setStatus(_A)
_RejectCpsHistDaysUnitCount_Type=Counter64
_RejectCpsHistDaysUnitCount_Object=MibTableColumn
rejectCpsHistDaysUnitCount=_RejectCpsHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,18,1,3),_RejectCpsHistDaysUnitCount_Type())
rejectCpsHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistDaysUnitCount.setStatus(_A)
_RejectCpsHistDaysTimestamp_Type=Unsigned32
_RejectCpsHistDaysTimestamp_Object=MibTableColumn
rejectCpsHistDaysTimestamp=_RejectCpsHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,18,1,4),_RejectCpsHistDaysTimestamp_Type())
rejectCpsHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectCpsHistDaysTimestamp.setStatus(_A)
_AcceptCpsHistSecondsTable_Object=MibTable
acceptCpsHistSecondsTable=_AcceptCpsHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,19))
if mibBuilder.loadTexts:acceptCpsHistSecondsTable.setStatus(_A)
_AcceptCpsHistSecondsEntry_Object=MibTableRow
acceptCpsHistSecondsEntry=_AcceptCpsHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,19,1))
acceptCpsHistSecondsEntry.setIndexNames((0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:acceptCpsHistSecondsEntry.setStatus(_A)
class _AcceptCpsHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptCpsHistSecondsGlobalID_Type.__name__=_E
_AcceptCpsHistSecondsGlobalID_Object=MibTableColumn
acceptCpsHistSecondsGlobalID=_AcceptCpsHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,19,1,1),_AcceptCpsHistSecondsGlobalID_Type())
acceptCpsHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistSecondsGlobalID.setStatus(_A)
_AcceptCpsHistSecondsIndex_Type=Unsigned32
_AcceptCpsHistSecondsIndex_Object=MibTableColumn
acceptCpsHistSecondsIndex=_AcceptCpsHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,19,1,2),_AcceptCpsHistSecondsIndex_Type())
acceptCpsHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistSecondsIndex.setStatus(_A)
_AcceptCpsHistSecondsUnitCount_Type=Counter64
_AcceptCpsHistSecondsUnitCount_Object=MibTableColumn
acceptCpsHistSecondsUnitCount=_AcceptCpsHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,19,1,3),_AcceptCpsHistSecondsUnitCount_Type())
acceptCpsHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistSecondsUnitCount.setStatus(_A)
_AcceptCpsHistSecondsTimestamp_Type=Unsigned32
_AcceptCpsHistSecondsTimestamp_Object=MibTableColumn
acceptCpsHistSecondsTimestamp=_AcceptCpsHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,19,1,4),_AcceptCpsHistSecondsTimestamp_Type())
acceptCpsHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistSecondsTimestamp.setStatus(_A)
_AcceptCpsHistMinutesTable_Object=MibTable
acceptCpsHistMinutesTable=_AcceptCpsHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,20))
if mibBuilder.loadTexts:acceptCpsHistMinutesTable.setStatus(_A)
_AcceptCpsHistMinutesEntry_Object=MibTableRow
acceptCpsHistMinutesEntry=_AcceptCpsHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,20,1))
acceptCpsHistMinutesEntry.setIndexNames((0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:acceptCpsHistMinutesEntry.setStatus(_A)
class _AcceptCpsHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptCpsHistMinutesGlobalID_Type.__name__=_E
_AcceptCpsHistMinutesGlobalID_Object=MibTableColumn
acceptCpsHistMinutesGlobalID=_AcceptCpsHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,20,1,1),_AcceptCpsHistMinutesGlobalID_Type())
acceptCpsHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistMinutesGlobalID.setStatus(_A)
_AcceptCpsHistMinutesIndex_Type=Unsigned32
_AcceptCpsHistMinutesIndex_Object=MibTableColumn
acceptCpsHistMinutesIndex=_AcceptCpsHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,20,1,2),_AcceptCpsHistMinutesIndex_Type())
acceptCpsHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistMinutesIndex.setStatus(_A)
_AcceptCpsHistMinutesUnitCount_Type=Counter64
_AcceptCpsHistMinutesUnitCount_Object=MibTableColumn
acceptCpsHistMinutesUnitCount=_AcceptCpsHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,20,1,3),_AcceptCpsHistMinutesUnitCount_Type())
acceptCpsHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistMinutesUnitCount.setStatus(_A)
_AcceptCpsHistMinutesTimestamp_Type=Unsigned32
_AcceptCpsHistMinutesTimestamp_Object=MibTableColumn
acceptCpsHistMinutesTimestamp=_AcceptCpsHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,20,1,4),_AcceptCpsHistMinutesTimestamp_Type())
acceptCpsHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistMinutesTimestamp.setStatus(_A)
_AcceptCpsHistHoursTable_Object=MibTable
acceptCpsHistHoursTable=_AcceptCpsHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,21))
if mibBuilder.loadTexts:acceptCpsHistHoursTable.setStatus(_A)
_AcceptCpsHistHoursEntry_Object=MibTableRow
acceptCpsHistHoursEntry=_AcceptCpsHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,21,1))
acceptCpsHistHoursEntry.setIndexNames((0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:acceptCpsHistHoursEntry.setStatus(_A)
class _AcceptCpsHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptCpsHistHoursGlobalID_Type.__name__=_E
_AcceptCpsHistHoursGlobalID_Object=MibTableColumn
acceptCpsHistHoursGlobalID=_AcceptCpsHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,21,1,1),_AcceptCpsHistHoursGlobalID_Type())
acceptCpsHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistHoursGlobalID.setStatus(_A)
_AcceptCpsHistHoursIndex_Type=Unsigned32
_AcceptCpsHistHoursIndex_Object=MibTableColumn
acceptCpsHistHoursIndex=_AcceptCpsHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,21,1,2),_AcceptCpsHistHoursIndex_Type())
acceptCpsHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistHoursIndex.setStatus(_A)
_AcceptCpsHistHoursUnitCount_Type=Counter64
_AcceptCpsHistHoursUnitCount_Object=MibTableColumn
acceptCpsHistHoursUnitCount=_AcceptCpsHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,21,1,3),_AcceptCpsHistHoursUnitCount_Type())
acceptCpsHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistHoursUnitCount.setStatus(_A)
_AcceptCpsHistHoursTimestamp_Type=Unsigned32
_AcceptCpsHistHoursTimestamp_Object=MibTableColumn
acceptCpsHistHoursTimestamp=_AcceptCpsHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,21,1,4),_AcceptCpsHistHoursTimestamp_Type())
acceptCpsHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistHoursTimestamp.setStatus(_A)
_AcceptCpsHistDaysTable_Object=MibTable
acceptCpsHistDaysTable=_AcceptCpsHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,22))
if mibBuilder.loadTexts:acceptCpsHistDaysTable.setStatus(_A)
_AcceptCpsHistDaysEntry_Object=MibTableRow
acceptCpsHistDaysEntry=_AcceptCpsHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,22,1))
acceptCpsHistDaysEntry.setIndexNames((0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:acceptCpsHistDaysEntry.setStatus(_A)
class _AcceptCpsHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptCpsHistDaysGlobalID_Type.__name__=_E
_AcceptCpsHistDaysGlobalID_Object=MibTableColumn
acceptCpsHistDaysGlobalID=_AcceptCpsHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,22,1,1),_AcceptCpsHistDaysGlobalID_Type())
acceptCpsHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistDaysGlobalID.setStatus(_A)
_AcceptCpsHistDaysIndex_Type=Unsigned32
_AcceptCpsHistDaysIndex_Object=MibTableColumn
acceptCpsHistDaysIndex=_AcceptCpsHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,22,1,2),_AcceptCpsHistDaysIndex_Type())
acceptCpsHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptCpsHistDaysIndex.setStatus(_A)
_AcceptCpsHistDaysUnitCount_Type=Counter64
_AcceptCpsHistDaysUnitCount_Object=MibTableColumn
acceptCpsHistDaysUnitCount=_AcceptCpsHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,22,1,3),_AcceptCpsHistDaysUnitCount_Type())
acceptCpsHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistDaysUnitCount.setStatus(_A)
_AcceptCpsHistDaysTimestamp_Type=Unsigned32
_AcceptCpsHistDaysTimestamp_Object=MibTableColumn
acceptCpsHistDaysTimestamp=_AcceptCpsHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,22,1,4),_AcceptCpsHistDaysTimestamp_Type())
acceptCpsHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptCpsHistDaysTimestamp.setStatus(_A)
_RejectEstHistSecondsTable_Object=MibTable
rejectEstHistSecondsTable=_RejectEstHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,25))
if mibBuilder.loadTexts:rejectEstHistSecondsTable.setStatus(_A)
_RejectEstHistSecondsEntry_Object=MibTableRow
rejectEstHistSecondsEntry=_RejectEstHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,25,1))
rejectEstHistSecondsEntry.setIndexNames((0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:rejectEstHistSecondsEntry.setStatus(_A)
class _RejectEstHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectEstHistSecondsGlobalID_Type.__name__=_E
_RejectEstHistSecondsGlobalID_Object=MibTableColumn
rejectEstHistSecondsGlobalID=_RejectEstHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,25,1,1),_RejectEstHistSecondsGlobalID_Type())
rejectEstHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistSecondsGlobalID.setStatus(_A)
_RejectEstHistSecondsIndex_Type=Unsigned32
_RejectEstHistSecondsIndex_Object=MibTableColumn
rejectEstHistSecondsIndex=_RejectEstHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,25,1,2),_RejectEstHistSecondsIndex_Type())
rejectEstHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistSecondsIndex.setStatus(_A)
_RejectEstHistSecondsUnitCount_Type=Counter64
_RejectEstHistSecondsUnitCount_Object=MibTableColumn
rejectEstHistSecondsUnitCount=_RejectEstHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,25,1,3),_RejectEstHistSecondsUnitCount_Type())
rejectEstHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistSecondsUnitCount.setStatus(_A)
_RejectEstHistSecondsTimestamp_Type=Unsigned32
_RejectEstHistSecondsTimestamp_Object=MibTableColumn
rejectEstHistSecondsTimestamp=_RejectEstHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,25,1,4),_RejectEstHistSecondsTimestamp_Type())
rejectEstHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistSecondsTimestamp.setStatus(_A)
_RejectEstHistMinutesTable_Object=MibTable
rejectEstHistMinutesTable=_RejectEstHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,26))
if mibBuilder.loadTexts:rejectEstHistMinutesTable.setStatus(_A)
_RejectEstHistMinutesEntry_Object=MibTableRow
rejectEstHistMinutesEntry=_RejectEstHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,26,1))
rejectEstHistMinutesEntry.setIndexNames((0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:rejectEstHistMinutesEntry.setStatus(_A)
class _RejectEstHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectEstHistMinutesGlobalID_Type.__name__=_E
_RejectEstHistMinutesGlobalID_Object=MibTableColumn
rejectEstHistMinutesGlobalID=_RejectEstHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,26,1,1),_RejectEstHistMinutesGlobalID_Type())
rejectEstHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistMinutesGlobalID.setStatus(_A)
_RejectEstHistMinutesIndex_Type=Unsigned32
_RejectEstHistMinutesIndex_Object=MibTableColumn
rejectEstHistMinutesIndex=_RejectEstHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,26,1,2),_RejectEstHistMinutesIndex_Type())
rejectEstHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistMinutesIndex.setStatus(_A)
_RejectEstHistMinutesUnitCount_Type=Counter64
_RejectEstHistMinutesUnitCount_Object=MibTableColumn
rejectEstHistMinutesUnitCount=_RejectEstHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,26,1,3),_RejectEstHistMinutesUnitCount_Type())
rejectEstHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistMinutesUnitCount.setStatus(_A)
_RejectEstHistMinutesTimestamp_Type=Unsigned32
_RejectEstHistMinutesTimestamp_Object=MibTableColumn
rejectEstHistMinutesTimestamp=_RejectEstHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,26,1,4),_RejectEstHistMinutesTimestamp_Type())
rejectEstHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistMinutesTimestamp.setStatus(_A)
_RejectEstHistHoursTable_Object=MibTable
rejectEstHistHoursTable=_RejectEstHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,27))
if mibBuilder.loadTexts:rejectEstHistHoursTable.setStatus(_A)
_RejectEstHistHoursEntry_Object=MibTableRow
rejectEstHistHoursEntry=_RejectEstHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,27,1))
rejectEstHistHoursEntry.setIndexNames((0,_B,_p),(0,_B,_q))
if mibBuilder.loadTexts:rejectEstHistHoursEntry.setStatus(_A)
class _RejectEstHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectEstHistHoursGlobalID_Type.__name__=_E
_RejectEstHistHoursGlobalID_Object=MibTableColumn
rejectEstHistHoursGlobalID=_RejectEstHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,27,1,1),_RejectEstHistHoursGlobalID_Type())
rejectEstHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistHoursGlobalID.setStatus(_A)
_RejectEstHistHoursIndex_Type=Unsigned32
_RejectEstHistHoursIndex_Object=MibTableColumn
rejectEstHistHoursIndex=_RejectEstHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,27,1,2),_RejectEstHistHoursIndex_Type())
rejectEstHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistHoursIndex.setStatus(_A)
_RejectEstHistHoursUnitCount_Type=Counter64
_RejectEstHistHoursUnitCount_Object=MibTableColumn
rejectEstHistHoursUnitCount=_RejectEstHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,27,1,3),_RejectEstHistHoursUnitCount_Type())
rejectEstHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistHoursUnitCount.setStatus(_A)
_RejectEstHistHoursTimestamp_Type=Unsigned32
_RejectEstHistHoursTimestamp_Object=MibTableColumn
rejectEstHistHoursTimestamp=_RejectEstHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,27,1,4),_RejectEstHistHoursTimestamp_Type())
rejectEstHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistHoursTimestamp.setStatus(_A)
_RejectEstHistDaysTable_Object=MibTable
rejectEstHistDaysTable=_RejectEstHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,28))
if mibBuilder.loadTexts:rejectEstHistDaysTable.setStatus(_A)
_RejectEstHistDaysEntry_Object=MibTableRow
rejectEstHistDaysEntry=_RejectEstHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,28,1))
rejectEstHistDaysEntry.setIndexNames((0,_B,_r),(0,_B,_s))
if mibBuilder.loadTexts:rejectEstHistDaysEntry.setStatus(_A)
class _RejectEstHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RejectEstHistDaysGlobalID_Type.__name__=_E
_RejectEstHistDaysGlobalID_Object=MibTableColumn
rejectEstHistDaysGlobalID=_RejectEstHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,28,1,1),_RejectEstHistDaysGlobalID_Type())
rejectEstHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistDaysGlobalID.setStatus(_A)
_RejectEstHistDaysIndex_Type=Unsigned32
_RejectEstHistDaysIndex_Object=MibTableColumn
rejectEstHistDaysIndex=_RejectEstHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,28,1,2),_RejectEstHistDaysIndex_Type())
rejectEstHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rejectEstHistDaysIndex.setStatus(_A)
_RejectEstHistDaysUnitCount_Type=Counter64
_RejectEstHistDaysUnitCount_Object=MibTableColumn
rejectEstHistDaysUnitCount=_RejectEstHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,28,1,3),_RejectEstHistDaysUnitCount_Type())
rejectEstHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistDaysUnitCount.setStatus(_A)
_RejectEstHistDaysTimestamp_Type=Unsigned32
_RejectEstHistDaysTimestamp_Object=MibTableColumn
rejectEstHistDaysTimestamp=_RejectEstHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,28,1,4),_RejectEstHistDaysTimestamp_Type())
rejectEstHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:rejectEstHistDaysTimestamp.setStatus(_A)
_AcceptEstHistSecondsTable_Object=MibTable
acceptEstHistSecondsTable=_AcceptEstHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,9,29))
if mibBuilder.loadTexts:acceptEstHistSecondsTable.setStatus(_A)
_AcceptEstHistSecondsEntry_Object=MibTableRow
acceptEstHistSecondsEntry=_AcceptEstHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,29,1))
acceptEstHistSecondsEntry.setIndexNames((0,_B,_t),(0,_B,_u))
if mibBuilder.loadTexts:acceptEstHistSecondsEntry.setStatus(_A)
class _AcceptEstHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptEstHistSecondsGlobalID_Type.__name__=_E
_AcceptEstHistSecondsGlobalID_Object=MibTableColumn
acceptEstHistSecondsGlobalID=_AcceptEstHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,29,1,1),_AcceptEstHistSecondsGlobalID_Type())
acceptEstHistSecondsGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistSecondsGlobalID.setStatus(_A)
_AcceptEstHistSecondsIndex_Type=Unsigned32
_AcceptEstHistSecondsIndex_Object=MibTableColumn
acceptEstHistSecondsIndex=_AcceptEstHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,29,1,2),_AcceptEstHistSecondsIndex_Type())
acceptEstHistSecondsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistSecondsIndex.setStatus(_A)
_AcceptEstHistSecondsUnitCount_Type=Counter64
_AcceptEstHistSecondsUnitCount_Object=MibTableColumn
acceptEstHistSecondsUnitCount=_AcceptEstHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,29,1,3),_AcceptEstHistSecondsUnitCount_Type())
acceptEstHistSecondsUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistSecondsUnitCount.setStatus(_A)
_AcceptEstHistSecondsTimestamp_Type=Unsigned32
_AcceptEstHistSecondsTimestamp_Object=MibTableColumn
acceptEstHistSecondsTimestamp=_AcceptEstHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,29,1,4),_AcceptEstHistSecondsTimestamp_Type())
acceptEstHistSecondsTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistSecondsTimestamp.setStatus(_A)
_AcceptEstHistMinutesTable_Object=MibTable
acceptEstHistMinutesTable=_AcceptEstHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,9,30))
if mibBuilder.loadTexts:acceptEstHistMinutesTable.setStatus(_A)
_AcceptEstHistMinutesEntry_Object=MibTableRow
acceptEstHistMinutesEntry=_AcceptEstHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,30,1))
acceptEstHistMinutesEntry.setIndexNames((0,_B,_v),(0,_B,_w))
if mibBuilder.loadTexts:acceptEstHistMinutesEntry.setStatus(_A)
class _AcceptEstHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptEstHistMinutesGlobalID_Type.__name__=_E
_AcceptEstHistMinutesGlobalID_Object=MibTableColumn
acceptEstHistMinutesGlobalID=_AcceptEstHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,30,1,1),_AcceptEstHistMinutesGlobalID_Type())
acceptEstHistMinutesGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistMinutesGlobalID.setStatus(_A)
_AcceptEstHistMinutesIndex_Type=Unsigned32
_AcceptEstHistMinutesIndex_Object=MibTableColumn
acceptEstHistMinutesIndex=_AcceptEstHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,30,1,2),_AcceptEstHistMinutesIndex_Type())
acceptEstHistMinutesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistMinutesIndex.setStatus(_A)
_AcceptEstHistMinutesUnitCount_Type=Counter64
_AcceptEstHistMinutesUnitCount_Object=MibTableColumn
acceptEstHistMinutesUnitCount=_AcceptEstHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,30,1,3),_AcceptEstHistMinutesUnitCount_Type())
acceptEstHistMinutesUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistMinutesUnitCount.setStatus(_A)
_AcceptEstHistMinutesTimestamp_Type=Unsigned32
_AcceptEstHistMinutesTimestamp_Object=MibTableColumn
acceptEstHistMinutesTimestamp=_AcceptEstHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,30,1,4),_AcceptEstHistMinutesTimestamp_Type())
acceptEstHistMinutesTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistMinutesTimestamp.setStatus(_A)
_AcceptEstHistHoursTable_Object=MibTable
acceptEstHistHoursTable=_AcceptEstHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,9,31))
if mibBuilder.loadTexts:acceptEstHistHoursTable.setStatus(_A)
_AcceptEstHistHoursEntry_Object=MibTableRow
acceptEstHistHoursEntry=_AcceptEstHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,31,1))
acceptEstHistHoursEntry.setIndexNames((0,_B,_x),(0,_B,_y))
if mibBuilder.loadTexts:acceptEstHistHoursEntry.setStatus(_A)
class _AcceptEstHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptEstHistHoursGlobalID_Type.__name__=_E
_AcceptEstHistHoursGlobalID_Object=MibTableColumn
acceptEstHistHoursGlobalID=_AcceptEstHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,31,1,1),_AcceptEstHistHoursGlobalID_Type())
acceptEstHistHoursGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistHoursGlobalID.setStatus(_A)
_AcceptEstHistHoursIndex_Type=Unsigned32
_AcceptEstHistHoursIndex_Object=MibTableColumn
acceptEstHistHoursIndex=_AcceptEstHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,31,1,2),_AcceptEstHistHoursIndex_Type())
acceptEstHistHoursIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistHoursIndex.setStatus(_A)
_AcceptEstHistHoursUnitCount_Type=Counter64
_AcceptEstHistHoursUnitCount_Object=MibTableColumn
acceptEstHistHoursUnitCount=_AcceptEstHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,31,1,3),_AcceptEstHistHoursUnitCount_Type())
acceptEstHistHoursUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistHoursUnitCount.setStatus(_A)
_AcceptEstHistHoursTimestamp_Type=Unsigned32
_AcceptEstHistHoursTimestamp_Object=MibTableColumn
acceptEstHistHoursTimestamp=_AcceptEstHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,31,1,4),_AcceptEstHistHoursTimestamp_Type())
acceptEstHistHoursTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistHoursTimestamp.setStatus(_A)
_AcceptEstHistDaysTable_Object=MibTable
acceptEstHistDaysTable=_AcceptEstHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,9,32))
if mibBuilder.loadTexts:acceptEstHistDaysTable.setStatus(_A)
_AcceptEstHistDaysEntry_Object=MibTableRow
acceptEstHistDaysEntry=_AcceptEstHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,9,32,1))
acceptEstHistDaysEntry.setIndexNames((0,_B,_z),(0,_B,_A0))
if mibBuilder.loadTexts:acceptEstHistDaysEntry.setStatus(_A)
class _AcceptEstHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AcceptEstHistDaysGlobalID_Type.__name__=_E
_AcceptEstHistDaysGlobalID_Object=MibTableColumn
acceptEstHistDaysGlobalID=_AcceptEstHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,9,32,1,1),_AcceptEstHistDaysGlobalID_Type())
acceptEstHistDaysGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistDaysGlobalID.setStatus(_A)
_AcceptEstHistDaysIndex_Type=Unsigned32
_AcceptEstHistDaysIndex_Object=MibTableColumn
acceptEstHistDaysIndex=_AcceptEstHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,9,32,1,2),_AcceptEstHistDaysIndex_Type())
acceptEstHistDaysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acceptEstHistDaysIndex.setStatus(_A)
_AcceptEstHistDaysUnitCount_Type=Counter64
_AcceptEstHistDaysUnitCount_Object=MibTableColumn
acceptEstHistDaysUnitCount=_AcceptEstHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,9,32,1,3),_AcceptEstHistDaysUnitCount_Type())
acceptEstHistDaysUnitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistDaysUnitCount.setStatus(_A)
_AcceptEstHistDaysTimestamp_Type=Unsigned32
_AcceptEstHistDaysTimestamp_Object=MibTableColumn
acceptEstHistDaysTimestamp=_AcceptEstHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,9,32,1,4),_AcceptEstHistDaysTimestamp_Type())
acceptEstHistDaysTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:acceptEstHistDaysTimestamp.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tpt-ddos':tpt_ddos,'rejectSynHistSecondsTable':rejectSynHistSecondsTable,'rejectSynHistSecondsEntry':rejectSynHistSecondsEntry,_F:rejectSynHistSecondsGlobalID,_G:rejectSynHistSecondsIndex,'rejectSynHistSecondsUnitCount':rejectSynHistSecondsUnitCount,'rejectSynHistSecondsTimestamp':rejectSynHistSecondsTimestamp,'rejectSynHistMinutesTable':rejectSynHistMinutesTable,'rejectSynHistMinutesEntry':rejectSynHistMinutesEntry,_H:rejectSynHistMinutesGlobalID,_I:rejectSynHistMinutesIndex,'rejectSynHistMinutesUnitCount':rejectSynHistMinutesUnitCount,'rejectSynHistMinutesTimestamp':rejectSynHistMinutesTimestamp,'rejectSynHistHoursTable':rejectSynHistHoursTable,'rejectSynHistHoursEntry':rejectSynHistHoursEntry,_J:rejectSynHistHoursGlobalID,_K:rejectSynHistHoursIndex,'rejectSynHistHoursUnitCount':rejectSynHistHoursUnitCount,'rejectSynHistHoursTimestamp':rejectSynHistHoursTimestamp,'rejectSynHistDaysTable':rejectSynHistDaysTable,'rejectSynHistDaysEntry':rejectSynHistDaysEntry,_L:rejectSynHistDaysGlobalID,_M:rejectSynHistDaysIndex,'rejectSynHistDaysUnitCount':rejectSynHistDaysUnitCount,'rejectSynHistDaysTimestamp':rejectSynHistDaysTimestamp,'proxyConnHistSecondsTable':proxyConnHistSecondsTable,'proxyConnHistSecondsEntry':proxyConnHistSecondsEntry,_N:proxyConnHistSecondsGlobalID,_O:proxyConnHistSecondsIndex,'proxyConnHistSecondsUnitCount':proxyConnHistSecondsUnitCount,'proxyConnHistSecondsTimestamp':proxyConnHistSecondsTimestamp,'proxyConnHistMinutesTable':proxyConnHistMinutesTable,'proxyConnHistMinutesEntry':proxyConnHistMinutesEntry,_P:proxyConnHistMinutesGlobalID,_Q:proxyConnHistMinutesIndex,'proxyConnHistMinutesUnitCount':proxyConnHistMinutesUnitCount,'proxyConnHistMinutesTimestamp':proxyConnHistMinutesTimestamp,'proxyConnHistHoursTable':proxyConnHistHoursTable,'proxyConnHistHoursEntry':proxyConnHistHoursEntry,_R:proxyConnHistHoursGlobalID,_S:proxyConnHistHoursIndex,'proxyConnHistHoursUnitCount':proxyConnHistHoursUnitCount,'proxyConnHistHoursTimestamp':proxyConnHistHoursTimestamp,'proxyConnHistDaysTable':proxyConnHistDaysTable,'proxyConnHistDaysEntry':proxyConnHistDaysEntry,_T:proxyConnHistDaysGlobalID,_U:proxyConnHistDaysIndex,'proxyConnHistDaysUnitCount':proxyConnHistDaysUnitCount,'proxyConnHistDaysTimestamp':proxyConnHistDaysTimestamp,'rejectCpsHistSecondsTable':rejectCpsHistSecondsTable,'rejectCpsHistSecondsEntry':rejectCpsHistSecondsEntry,_V:rejectCpsHistSecondsGlobalID,_W:rejectCpsHistSecondsIndex,'rejectCpsHistSecondsUnitCount':rejectCpsHistSecondsUnitCount,'rejectCpsHistSecondsTimestamp':rejectCpsHistSecondsTimestamp,'rejectCpsHistMinutesTable':rejectCpsHistMinutesTable,'rejectCpsHistMinutesEntry':rejectCpsHistMinutesEntry,_X:rejectCpsHistMinutesGlobalID,_Y:rejectCpsHistMinutesIndex,'rejectCpsHistMinutesUnitCount':rejectCpsHistMinutesUnitCount,'rejectCpsHistMinutesTimestamp':rejectCpsHistMinutesTimestamp,'rejectCpsHistHoursTable':rejectCpsHistHoursTable,'rejectCpsHistHoursEntry':rejectCpsHistHoursEntry,_Z:rejectCpsHistHoursGlobalID,_a:rejectCpsHistHoursIndex,'rejectCpsHistHoursUnitCount':rejectCpsHistHoursUnitCount,'rejectCpsHistHoursTimestamp':rejectCpsHistHoursTimestamp,'rejectCpsHistDaysTable':rejectCpsHistDaysTable,'rejectCpsHistDaysEntry':rejectCpsHistDaysEntry,_b:rejectCpsHistDaysGlobalID,_c:rejectCpsHistDaysIndex,'rejectCpsHistDaysUnitCount':rejectCpsHistDaysUnitCount,'rejectCpsHistDaysTimestamp':rejectCpsHistDaysTimestamp,'acceptCpsHistSecondsTable':acceptCpsHistSecondsTable,'acceptCpsHistSecondsEntry':acceptCpsHistSecondsEntry,_d:acceptCpsHistSecondsGlobalID,_e:acceptCpsHistSecondsIndex,'acceptCpsHistSecondsUnitCount':acceptCpsHistSecondsUnitCount,'acceptCpsHistSecondsTimestamp':acceptCpsHistSecondsTimestamp,'acceptCpsHistMinutesTable':acceptCpsHistMinutesTable,'acceptCpsHistMinutesEntry':acceptCpsHistMinutesEntry,_f:acceptCpsHistMinutesGlobalID,_g:acceptCpsHistMinutesIndex,'acceptCpsHistMinutesUnitCount':acceptCpsHistMinutesUnitCount,'acceptCpsHistMinutesTimestamp':acceptCpsHistMinutesTimestamp,'acceptCpsHistHoursTable':acceptCpsHistHoursTable,'acceptCpsHistHoursEntry':acceptCpsHistHoursEntry,_h:acceptCpsHistHoursGlobalID,_i:acceptCpsHistHoursIndex,'acceptCpsHistHoursUnitCount':acceptCpsHistHoursUnitCount,'acceptCpsHistHoursTimestamp':acceptCpsHistHoursTimestamp,'acceptCpsHistDaysTable':acceptCpsHistDaysTable,'acceptCpsHistDaysEntry':acceptCpsHistDaysEntry,_j:acceptCpsHistDaysGlobalID,_k:acceptCpsHistDaysIndex,'acceptCpsHistDaysUnitCount':acceptCpsHistDaysUnitCount,'acceptCpsHistDaysTimestamp':acceptCpsHistDaysTimestamp,'rejectEstHistSecondsTable':rejectEstHistSecondsTable,'rejectEstHistSecondsEntry':rejectEstHistSecondsEntry,_l:rejectEstHistSecondsGlobalID,_m:rejectEstHistSecondsIndex,'rejectEstHistSecondsUnitCount':rejectEstHistSecondsUnitCount,'rejectEstHistSecondsTimestamp':rejectEstHistSecondsTimestamp,'rejectEstHistMinutesTable':rejectEstHistMinutesTable,'rejectEstHistMinutesEntry':rejectEstHistMinutesEntry,_n:rejectEstHistMinutesGlobalID,_o:rejectEstHistMinutesIndex,'rejectEstHistMinutesUnitCount':rejectEstHistMinutesUnitCount,'rejectEstHistMinutesTimestamp':rejectEstHistMinutesTimestamp,'rejectEstHistHoursTable':rejectEstHistHoursTable,'rejectEstHistHoursEntry':rejectEstHistHoursEntry,_p:rejectEstHistHoursGlobalID,_q:rejectEstHistHoursIndex,'rejectEstHistHoursUnitCount':rejectEstHistHoursUnitCount,'rejectEstHistHoursTimestamp':rejectEstHistHoursTimestamp,'rejectEstHistDaysTable':rejectEstHistDaysTable,'rejectEstHistDaysEntry':rejectEstHistDaysEntry,_r:rejectEstHistDaysGlobalID,_s:rejectEstHistDaysIndex,'rejectEstHistDaysUnitCount':rejectEstHistDaysUnitCount,'rejectEstHistDaysTimestamp':rejectEstHistDaysTimestamp,'acceptEstHistSecondsTable':acceptEstHistSecondsTable,'acceptEstHistSecondsEntry':acceptEstHistSecondsEntry,_t:acceptEstHistSecondsGlobalID,_u:acceptEstHistSecondsIndex,'acceptEstHistSecondsUnitCount':acceptEstHistSecondsUnitCount,'acceptEstHistSecondsTimestamp':acceptEstHistSecondsTimestamp,'acceptEstHistMinutesTable':acceptEstHistMinutesTable,'acceptEstHistMinutesEntry':acceptEstHistMinutesEntry,_v:acceptEstHistMinutesGlobalID,_w:acceptEstHistMinutesIndex,'acceptEstHistMinutesUnitCount':acceptEstHistMinutesUnitCount,'acceptEstHistMinutesTimestamp':acceptEstHistMinutesTimestamp,'acceptEstHistHoursTable':acceptEstHistHoursTable,'acceptEstHistHoursEntry':acceptEstHistHoursEntry,_x:acceptEstHistHoursGlobalID,_y:acceptEstHistHoursIndex,'acceptEstHistHoursUnitCount':acceptEstHistHoursUnitCount,'acceptEstHistHoursTimestamp':acceptEstHistHoursTimestamp,'acceptEstHistDaysTable':acceptEstHistDaysTable,'acceptEstHistDaysEntry':acceptEstHistDaysEntry,_z:acceptEstHistDaysGlobalID,_A0:acceptEstHistDaysIndex,'acceptEstHistDaysUnitCount':acceptEstHistDaysUnitCount,'acceptEstHistDaysTimestamp':acceptEstHistDaysTimestamp})