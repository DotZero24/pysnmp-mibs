_G='h3cRasMsgIndex'
_F='h3cH245MsgIndex'
_E='h3cH225MsgIndex'
_D='not-accessible'
_C='A3COM-HUAWEI-VOH323CALLSTAT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoiceH323CallStat=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,11))
if mibBuilder.loadTexts:h3cVoiceH323CallStat.setRevisions(('2005-03-15 00:00',))
_H3cVOIPH225StatTable_Object=MibTable
h3cVOIPH225StatTable=_H3cVOIPH225StatTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1))
if mibBuilder.loadTexts:h3cVOIPH225StatTable.setStatus(_A)
_H3cVOIPH225StatEntry_Object=MibTableRow
h3cVOIPH225StatEntry=_H3cVOIPH225StatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1,1))
h3cVOIPH225StatEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cVOIPH225StatEntry.setStatus(_A)
_H3cH225MsgIndex_Type=Integer32
_H3cH225MsgIndex_Object=MibTableColumn
h3cH225MsgIndex=_H3cH225MsgIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1,1,1),_H3cH225MsgIndex_Type())
h3cH225MsgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cH225MsgIndex.setStatus(_A)
_H3cH225MsgName_Type=OctetString
_H3cH225MsgName_Object=MibTableColumn
h3cH225MsgName=_H3cH225MsgName_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1,1,2),_H3cH225MsgName_Type())
h3cH225MsgName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH225MsgName.setStatus(_A)
_H3cH225MsgSend_Type=Counter32
_H3cH225MsgSend_Object=MibTableColumn
h3cH225MsgSend=_H3cH225MsgSend_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1,1,3),_H3cH225MsgSend_Type())
h3cH225MsgSend.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH225MsgSend.setStatus(_A)
_H3cH225MsgReceive_Type=Counter32
_H3cH225MsgReceive_Object=MibTableColumn
h3cH225MsgReceive=_H3cH225MsgReceive_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,1,1,4),_H3cH225MsgReceive_Type())
h3cH225MsgReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH225MsgReceive.setStatus(_A)
_H3cVOIPH245StatTable_Object=MibTable
h3cVOIPH245StatTable=_H3cVOIPH245StatTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2))
if mibBuilder.loadTexts:h3cVOIPH245StatTable.setStatus(_A)
_H3cVOIPH245StatEntry_Object=MibTableRow
h3cVOIPH245StatEntry=_H3cVOIPH245StatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2,1))
h3cVOIPH245StatEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cVOIPH245StatEntry.setStatus(_A)
_H3cH245MsgIndex_Type=Integer32
_H3cH245MsgIndex_Object=MibTableColumn
h3cH245MsgIndex=_H3cH245MsgIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2,1,1),_H3cH245MsgIndex_Type())
h3cH245MsgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cH245MsgIndex.setStatus(_A)
_H3cH245MsgName_Type=OctetString
_H3cH245MsgName_Object=MibTableColumn
h3cH245MsgName=_H3cH245MsgName_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2,1,2),_H3cH245MsgName_Type())
h3cH245MsgName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH245MsgName.setStatus(_A)
_H3cH245MsgSend_Type=Counter32
_H3cH245MsgSend_Object=MibTableColumn
h3cH245MsgSend=_H3cH245MsgSend_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2,1,3),_H3cH245MsgSend_Type())
h3cH245MsgSend.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH245MsgSend.setStatus(_A)
_H3cH245MsgReceive_Type=Counter32
_H3cH245MsgReceive_Object=MibTableColumn
h3cH245MsgReceive=_H3cH245MsgReceive_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,2,1,4),_H3cH245MsgReceive_Type())
h3cH245MsgReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cH245MsgReceive.setStatus(_A)
_H3cVOIPRasStatTable_Object=MibTable
h3cVOIPRasStatTable=_H3cVOIPRasStatTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3))
if mibBuilder.loadTexts:h3cVOIPRasStatTable.setStatus(_A)
_H3cVOIPRasStatEntry_Object=MibTableRow
h3cVOIPRasStatEntry=_H3cVOIPRasStatEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3,1))
h3cVOIPRasStatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:h3cVOIPRasStatEntry.setStatus(_A)
_H3cRasMsgIndex_Type=Integer32
_H3cRasMsgIndex_Object=MibTableColumn
h3cRasMsgIndex=_H3cRasMsgIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3,1,1),_H3cRasMsgIndex_Type())
h3cRasMsgIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRasMsgIndex.setStatus(_A)
_H3cRasMsgName_Type=OctetString
_H3cRasMsgName_Object=MibTableColumn
h3cRasMsgName=_H3cRasMsgName_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3,1,2),_H3cRasMsgName_Type())
h3cRasMsgName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRasMsgName.setStatus(_A)
_H3cRasMsgSend_Type=Counter32
_H3cRasMsgSend_Object=MibTableColumn
h3cRasMsgSend=_H3cRasMsgSend_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3,1,3),_H3cRasMsgSend_Type())
h3cRasMsgSend.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRasMsgSend.setStatus(_A)
_H3cRasMsgReceive_Type=Counter32
_H3cRasMsgReceive_Object=MibTableColumn
h3cRasMsgReceive=_H3cRasMsgReceive_Object((1,3,6,1,4,1,43,45,1,10,2,39,11,3,1,4),_H3cRasMsgReceive_Type())
h3cRasMsgReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRasMsgReceive.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cVoiceH323CallStat':h3cVoiceH323CallStat,'h3cVOIPH225StatTable':h3cVOIPH225StatTable,'h3cVOIPH225StatEntry':h3cVOIPH225StatEntry,_E:h3cH225MsgIndex,'h3cH225MsgName':h3cH225MsgName,'h3cH225MsgSend':h3cH225MsgSend,'h3cH225MsgReceive':h3cH225MsgReceive,'h3cVOIPH245StatTable':h3cVOIPH245StatTable,'h3cVOIPH245StatEntry':h3cVOIPH245StatEntry,_F:h3cH245MsgIndex,'h3cH245MsgName':h3cH245MsgName,'h3cH245MsgSend':h3cH245MsgSend,'h3cH245MsgReceive':h3cH245MsgReceive,'h3cVOIPRasStatTable':h3cVOIPRasStatTable,'h3cVOIPRasStatEntry':h3cVOIPRasStatEntry,_G:h3cRasMsgIndex,'h3cRasMsgName':h3cRasMsgName,'h3cRasMsgSend':h3cRasMsgSend,'h3cRasMsgReceive':h3cRasMsgReceive})