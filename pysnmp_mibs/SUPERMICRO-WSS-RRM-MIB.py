_G='disable'
_F='global'
_E='fsRrmRadioType'
_D='SUPERMICRO-WSS-RRM-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsRrm=ModuleIdentity((1,3,6,1,4,1,10876,101,2,84))
if mibBuilder.loadTexts:fsRrm.setRevisions(('2013-02-15 00:00',))
_FsRrmManagment_ObjectIdentity=ObjectIdentity
fsRrmManagment=_FsRrmManagment_ObjectIdentity((1,3,6,1,4,1,10876,101,2,84,1))
_FsRrmConfigTable_Object=MibTable
fsRrmConfigTable=_FsRrmConfigTable_Object((1,3,6,1,4,1,10876,101,2,84,1,1))
if mibBuilder.loadTexts:fsRrmConfigTable.setStatus(_A)
_FsRrmConfigEntry_Object=MibTableRow
fsRrmConfigEntry=_FsRrmConfigEntry_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1))
fsRrmConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsRrmConfigEntry.setStatus(_A)
class _FsRrmRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot11a',1),('dot11b',2)))
_FsRrmRadioType_Type.__name__=_B
_FsRrmRadioType_Object=MibTableColumn
fsRrmRadioType=_FsRrmRadioType_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,1),_FsRrmRadioType_Type())
fsRrmRadioType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsRrmRadioType.setStatus(_A)
class _FsRrmDcaMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('perAP',2),(_G,3)))
_FsRrmDcaMode_Type.__name__=_B
_FsRrmDcaMode_Object=MibTableColumn
fsRrmDcaMode=_FsRrmDcaMode_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,2),_FsRrmDcaMode_Type())
fsRrmDcaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrmDcaMode.setStatus(_A)
class _FsRrmDcaChannelSelectionMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('once',2),('off',3)))
_FsRrmDcaChannelSelectionMode_Type.__name__=_B
_FsRrmDcaChannelSelectionMode_Object=MibTableColumn
fsRrmDcaChannelSelectionMode=_FsRrmDcaChannelSelectionMode_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,3),_FsRrmDcaChannelSelectionMode_Type())
fsRrmDcaChannelSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrmDcaChannelSelectionMode.setStatus(_A)
class _FsRrmTpcMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('perAP',2),(_G,3)))
_FsRrmTpcMode_Type.__name__=_B
_FsRrmTpcMode_Object=MibTableColumn
fsRrmTpcMode=_FsRrmTpcMode_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,4),_FsRrmTpcMode_Type())
fsRrmTpcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrmTpcMode.setStatus(_A)
class _FsRrmTpcSelectionMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('once',2),('off',3)))
_FsRrmTpcSelectionMode_Type.__name__=_B
_FsRrmTpcSelectionMode_Object=MibTableColumn
fsRrmTpcSelectionMode=_FsRrmTpcSelectionMode_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,5),_FsRrmTpcSelectionMode_Type())
fsRrmTpcSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrmTpcSelectionMode.setStatus(_A)
_FsRrmRowStatus_Type=RowStatus
_FsRrmRowStatus_Object=MibTableColumn
fsRrmRowStatus=_FsRrmRowStatus_Object((1,3,6,1,4,1,10876,101,2,84,1,1,1,6),_FsRrmRowStatus_Type())
fsRrmRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsRrmRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsRrm':fsRrm,'fsRrmManagment':fsRrmManagment,'fsRrmConfigTable':fsRrmConfigTable,'fsRrmConfigEntry':fsRrmConfigEntry,_E:fsRrmRadioType,'fsRrmDcaMode':fsRrmDcaMode,'fsRrmDcaChannelSelectionMode':fsRrmDcaChannelSelectionMode,'fsRrmTpcMode':fsRrmTpcMode,'fsRrmTpcSelectionMode':fsRrmTpcSelectionMode,'fsRrmRowStatus':fsRrmRowStatus})