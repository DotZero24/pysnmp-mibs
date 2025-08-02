_E='loadIndex'
_D='AT-LOADER-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
loader=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,48))
if mibBuilder.loadTexts:loader.setRevisions(('2007-02-07 10:10','2006-06-28 12:22'))
_LoadTable_Object=MibTable
loadTable=_LoadTable_Object((1,3,6,1,4,1,207,8,4,4,4,48,1))
if mibBuilder.loadTexts:loadTable.setStatus(_A)
_LoadEntry_Object=MibTableRow
loadEntry=_LoadEntry_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1))
loadEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:loadEntry.setStatus(_A)
class _LoadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_LoadIndex_Type.__name__=_C
_LoadIndex_Object=MibTableColumn
loadIndex=_LoadIndex_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1,1),_LoadIndex_Type())
loadIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:loadIndex.setStatus(_A)
_LoadServer_Type=IpAddress
_LoadServer_Object=MibTableColumn
loadServer=_LoadServer_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1,2),_LoadServer_Type())
loadServer.setMaxAccess(_B)
if mibBuilder.loadTexts:loadServer.setStatus(_A)
class _LoadDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undefined',1),('nvs',2),('flash',3)))
_LoadDestination_Type.__name__=_C
_LoadDestination_Object=MibTableColumn
loadDestination=_LoadDestination_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1,3),_LoadDestination_Type())
loadDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:loadDestination.setStatus(_A)
_LoadFilename_Type=DisplayString
_LoadFilename_Object=MibTableColumn
loadFilename=_LoadFilename_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1,4),_LoadFilename_Type())
loadFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFilename.setStatus(_A)
_LoadDelay_Type=Integer32
_LoadDelay_Object=MibTableColumn
loadDelay=_LoadDelay_Object((1,3,6,1,4,1,207,8,4,4,4,48,1,1,5),_LoadDelay_Type())
loadDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:loadDelay.setStatus(_A)
class _LoadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('idle',1),('wait',2),('loading',3),('complete',4),('reset',5),('actionload',6),('actionstop',7),('actionupload',8)))
_LoadStatus_Type.__name__=_C
_LoadStatus_Object=MibScalar
loadStatus=_LoadStatus_Object((1,3,6,1,4,1,207,8,4,4,4,48,2),_LoadStatus_Type())
loadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:loadStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'loader':loader,'loadTable':loadTable,'loadEntry':loadEntry,_E:loadIndex,'loadServer':loadServer,'loadDestination':loadDestination,'loadFilename':loadFilename,'loadDelay':loadDelay,'loadStatus':loadStatus})