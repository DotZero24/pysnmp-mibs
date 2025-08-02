_J='modemScriptName'
_I='modemDialerString'
_H='modemDialerIfIndex'
_G='answer'
_F='read-only'
_E='modemIfIndex'
_D='MAIPU-MODEM-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mpModemMib=ModuleIdentity((1,3,6,1,4,1,5651,3,15))
_ModemConfTable_Object=MibTable
modemConfTable=_ModemConfTable_Object((1,3,6,1,4,1,5651,3,15,1))
if mibBuilder.loadTexts:modemConfTable.setStatus(_A)
_ModemConfEntry_Object=MibTableRow
modemConfEntry=_ModemConfEntry_Object((1,3,6,1,4,1,5651,3,15,1,1))
modemConfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:modemConfEntry.setStatus(_A)
_ModemIfIndex_Type=Integer32
_ModemIfIndex_Object=MibTableColumn
modemIfIndex=_ModemIfIndex_Object((1,3,6,1,4,1,5651,3,15,1,1,1),_ModemIfIndex_Type())
modemIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:modemIfIndex.setStatus(_A)
class _ModemLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inner',1),('outer',2),('noOuter',3)))
_ModemLocation_Type.__name__=_C
_ModemLocation_Object=MibTableColumn
modemLocation=_ModemLocation_Object((1,3,6,1,4,1,5651,3,15,1,1,2),_ModemLocation_Type())
modemLocation.setMaxAccess('read-write')
if mibBuilder.loadTexts:modemLocation.setStatus(_A)
class _ModemActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ModemActive_Type.__name__=_C
_ModemActive_Object=MibTableColumn
modemActive=_ModemActive_Object((1,3,6,1,4,1,5651,3,15,1,1,3),_ModemActive_Type())
modemActive.setMaxAccess(_B)
if mibBuilder.loadTexts:modemActive.setStatus(_A)
class _ModemLine_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leased',1),('nonLeased',2)))
_ModemLine_Type.__name__=_C
_ModemLine_Object=MibTableColumn
modemLine=_ModemLine_Object((1,3,6,1,4,1,5651,3,15,1,1,4),_ModemLine_Type())
modemLine.setMaxAccess(_B)
if mibBuilder.loadTexts:modemLine.setStatus(_A)
class _ModemParty_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('originate',1),(_G,2),('none',3)))
_ModemParty_Type.__name__=_C
_ModemParty_Object=MibTableColumn
modemParty=_ModemParty_Object((1,3,6,1,4,1,5651,3,15,1,1,5),_ModemParty_Type())
modemParty.setMaxAccess(_B)
if mibBuilder.loadTexts:modemParty.setStatus(_A)
class _ModemAsyncMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('buffer',1),('direct',2),('errorCorrect',3)))
_ModemAsyncMode_Type.__name__=_C
_ModemAsyncMode_Object=MibTableColumn
modemAsyncMode=_ModemAsyncMode_Object((1,3,6,1,4,1,5651,3,15,1,1,6),_ModemAsyncMode_Type())
modemAsyncMode.setMaxAccess(_B)
if mibBuilder.loadTexts:modemAsyncMode.setStatus(_A)
class _ModemClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internal',1),('external',2),('slave',3)))
_ModemClockMode_Type.__name__=_C
_ModemClockMode_Object=MibTableColumn
modemClockMode=_ModemClockMode_Object((1,3,6,1,4,1,5651,3,15,1,1,7),_ModemClockMode_Type())
modemClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:modemClockMode.setStatus(_A)
_ModemClockRate_Type=Integer32
_ModemClockRate_Object=MibTableColumn
modemClockRate=_ModemClockRate_Object((1,3,6,1,4,1,5651,3,15,1,1,8),_ModemClockRate_Type())
modemClockRate.setMaxAccess(_B)
if mibBuilder.loadTexts:modemClockRate.setStatus(_A)
class _ModemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unconfig',1),('idle',2),('atMode',3),('dialout',4),(_G,5),('connect',6),('config',7),('hangUp',8)))
_ModemStatus_Type.__name__=_C
_ModemStatus_Object=MibTableColumn
modemStatus=_ModemStatus_Object((1,3,6,1,4,1,5651,3,15,1,1,9),_ModemStatus_Type())
modemStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:modemStatus.setStatus(_A)
_ModemDialerTable_Object=MibTable
modemDialerTable=_ModemDialerTable_Object((1,3,6,1,4,1,5651,3,15,2))
if mibBuilder.loadTexts:modemDialerTable.setStatus(_A)
_ModemDialerEntry_Object=MibTableRow
modemDialerEntry=_ModemDialerEntry_Object((1,3,6,1,4,1,5651,3,15,2,1))
modemDialerEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:modemDialerEntry.setStatus(_A)
_ModemDialerIfIndex_Type=Integer32
_ModemDialerIfIndex_Object=MibTableColumn
modemDialerIfIndex=_ModemDialerIfIndex_Object((1,3,6,1,4,1,5651,3,15,2,1,1),_ModemDialerIfIndex_Type())
modemDialerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:modemDialerIfIndex.setStatus(_A)
_ModemDialerString_Type=OctetString
_ModemDialerString_Object=MibTableColumn
modemDialerString=_ModemDialerString_Object((1,3,6,1,4,1,5651,3,15,2,1,2),_ModemDialerString_Type())
modemDialerString.setMaxAccess(_B)
if mibBuilder.loadTexts:modemDialerString.setStatus(_A)
_ModemDialerStatus_Type=RowStatus
_ModemDialerStatus_Object=MibTableColumn
modemDialerStatus=_ModemDialerStatus_Object((1,3,6,1,4,1,5651,3,15,2,1,3),_ModemDialerStatus_Type())
modemDialerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:modemDialerStatus.setStatus(_A)
_ModemScriptTable_Object=MibTable
modemScriptTable=_ModemScriptTable_Object((1,3,6,1,4,1,5651,3,15,3))
if mibBuilder.loadTexts:modemScriptTable.setStatus(_A)
_ModemScriptEntry_Object=MibTableRow
modemScriptEntry=_ModemScriptEntry_Object((1,3,6,1,4,1,5651,3,15,3,1))
modemScriptEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:modemScriptEntry.setStatus(_A)
_ModemScriptName_Type=OctetString
_ModemScriptName_Object=MibTableColumn
modemScriptName=_ModemScriptName_Object((1,3,6,1,4,1,5651,3,15,3,1,1),_ModemScriptName_Type())
modemScriptName.setMaxAccess(_B)
if mibBuilder.loadTexts:modemScriptName.setStatus(_A)
_ModemScriptString_Type=OctetString
_ModemScriptString_Object=MibTableColumn
modemScriptString=_ModemScriptString_Object((1,3,6,1,4,1,5651,3,15,3,1,2),_ModemScriptString_Type())
modemScriptString.setMaxAccess(_B)
if mibBuilder.loadTexts:modemScriptString.setStatus(_A)
_ModemScriptStatus_Type=RowStatus
_ModemScriptStatus_Object=MibTableColumn
modemScriptStatus=_ModemScriptStatus_Object((1,3,6,1,4,1,5651,3,15,3,1,3),_ModemScriptStatus_Type())
modemScriptStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:modemScriptStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mpModemMib':mpModemMib,'modemConfTable':modemConfTable,'modemConfEntry':modemConfEntry,_E:modemIfIndex,'modemLocation':modemLocation,'modemActive':modemActive,'modemLine':modemLine,'modemParty':modemParty,'modemAsyncMode':modemAsyncMode,'modemClockMode':modemClockMode,'modemClockRate':modemClockRate,'modemStatus':modemStatus,'modemDialerTable':modemDialerTable,'modemDialerEntry':modemDialerEntry,_H:modemDialerIfIndex,_I:modemDialerString,'modemDialerStatus':modemDialerStatus,'modemScriptTable':modemScriptTable,'modemScriptEntry':modemScriptEntry,_J:modemScriptName,'modemScriptString':modemScriptString,'modemScriptStatus':modemScriptStatus})