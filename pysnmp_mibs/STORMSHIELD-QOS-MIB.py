_E='snsQosEntryIndex'
_D='STORMSHIELD-QOS-MIB'
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
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsQos=ModuleIdentity((1,3,6,1,4,1,11256,1,15))
if mibBuilder.loadTexts:snsQos.setRevisions(('2017-02-20 00:00',))
_SnsQosStatsTable_Object=MibTable
snsQosStatsTable=_SnsQosStatsTable_Object((1,3,6,1,4,1,11256,1,15,1))
if mibBuilder.loadTexts:snsQosStatsTable.setStatus(_A)
_SnsQosStatsEntry_Object=MibTableRow
snsQosStatsEntry=_SnsQosStatsEntry_Object((1,3,6,1,4,1,11256,1,15,1,1))
snsQosStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsQosStatsEntry.setStatus(_A)
class _SnsQosEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsQosEntryIndex_Type.__name__=_C
_SnsQosEntryIndex_Object=MibTableColumn
snsQosEntryIndex=_SnsQosEntryIndex_Object((1,3,6,1,4,1,11256,1,15,1,1,1),_SnsQosEntryIndex_Type())
snsQosEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryIndex.setStatus(_A)
_SnsQosEntryName_Type=DisplayString
_SnsQosEntryName_Object=MibTableColumn
snsQosEntryName=_SnsQosEntryName_Object((1,3,6,1,4,1,11256,1,15,1,1,2),_SnsQosEntryName_Type())
snsQosEntryName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryName.setStatus(_A)
_SnsQosEntryType_Type=DisplayString
_SnsQosEntryType_Object=MibTableColumn
snsQosEntryType=_SnsQosEntryType_Object((1,3,6,1,4,1,11256,1,15,1,1,3),_SnsQosEntryType_Type())
snsQosEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryType.setStatus(_A)
_SnsQosEntryInCounter_Type=Counter64
_SnsQosEntryInCounter_Object=MibTableColumn
snsQosEntryInCounter=_SnsQosEntryInCounter_Object((1,3,6,1,4,1,11256,1,15,1,1,4),_SnsQosEntryInCounter_Type())
snsQosEntryInCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryInCounter.setStatus(_A)
_SnsQosEntryInMaxPeak_Type=Counter64
_SnsQosEntryInMaxPeak_Object=MibTableColumn
snsQosEntryInMaxPeak=_SnsQosEntryInMaxPeak_Object((1,3,6,1,4,1,11256,1,15,1,1,5),_SnsQosEntryInMaxPeak_Type())
snsQosEntryInMaxPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryInMaxPeak.setStatus(_A)
_SnsQosEntryInSpeedLimit_Type=Counter64
_SnsQosEntryInSpeedLimit_Object=MibTableColumn
snsQosEntryInSpeedLimit=_SnsQosEntryInSpeedLimit_Object((1,3,6,1,4,1,11256,1,15,1,1,6),_SnsQosEntryInSpeedLimit_Type())
snsQosEntryInSpeedLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryInSpeedLimit.setStatus(_A)
_SnsQosEntryOutCounter_Type=Counter64
_SnsQosEntryOutCounter_Object=MibTableColumn
snsQosEntryOutCounter=_SnsQosEntryOutCounter_Object((1,3,6,1,4,1,11256,1,15,1,1,7),_SnsQosEntryOutCounter_Type())
snsQosEntryOutCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryOutCounter.setStatus(_A)
_SnsQosEntryOutMaxPeak_Type=Counter64
_SnsQosEntryOutMaxPeak_Object=MibTableColumn
snsQosEntryOutMaxPeak=_SnsQosEntryOutMaxPeak_Object((1,3,6,1,4,1,11256,1,15,1,1,8),_SnsQosEntryOutMaxPeak_Type())
snsQosEntryOutMaxPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryOutMaxPeak.setStatus(_A)
_SnsQosEntryOutSpeedLimit_Type=Counter64
_SnsQosEntryOutSpeedLimit_Object=MibTableColumn
snsQosEntryOutSpeedLimit=_SnsQosEntryOutSpeedLimit_Object((1,3,6,1,4,1,11256,1,15,1,1,9),_SnsQosEntryOutSpeedLimit_Type())
snsQosEntryOutSpeedLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryOutSpeedLimit.setStatus(_A)
_SnsQosEntryComment_Type=DisplayString
_SnsQosEntryComment_Object=MibTableColumn
snsQosEntryComment=_SnsQosEntryComment_Object((1,3,6,1,4,1,11256,1,15,1,1,10),_SnsQosEntryComment_Type())
snsQosEntryComment.setMaxAccess(_B)
if mibBuilder.loadTexts:snsQosEntryComment.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsQos':snsQos,'snsQosStatsTable':snsQosStatsTable,'snsQosStatsEntry':snsQosStatsEntry,_E:snsQosEntryIndex,'snsQosEntryName':snsQosEntryName,'snsQosEntryType':snsQosEntryType,'snsQosEntryInCounter':snsQosEntryInCounter,'snsQosEntryInMaxPeak':snsQosEntryInMaxPeak,'snsQosEntryInSpeedLimit':snsQosEntryInSpeedLimit,'snsQosEntryOutCounter':snsQosEntryOutCounter,'snsQosEntryOutMaxPeak':snsQosEntryOutMaxPeak,'snsQosEntryOutSpeedLimit':snsQosEntryOutSpeedLimit,'snsQosEntryComment':snsQosEntryComment})