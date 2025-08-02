_F='dlmodIndex'
_E='UCD-DLMOD-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ucdExperimental,=mibBuilder.importSymbols('UCD-SNMP-MIB','ucdExperimental')
ucdDlmodMIB=ModuleIdentity((1,3,6,1,4,1,2021,13,14))
if mibBuilder.loadTexts:ucdDlmodMIB.setRevisions(('2000-01-26 00:00','1999-12-10 00:00'))
_DlmodNextIndex_Type=Integer32
_DlmodNextIndex_Object=MibScalar
dlmodNextIndex=_DlmodNextIndex_Object((1,3,6,1,4,1,2021,13,14,1),_DlmodNextIndex_Type())
dlmodNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dlmodNextIndex.setStatus(_A)
_DlmodTable_Object=MibTable
dlmodTable=_DlmodTable_Object((1,3,6,1,4,1,2021,13,14,2))
if mibBuilder.loadTexts:dlmodTable.setStatus(_A)
_DlmodEntry_Object=MibTableRow
dlmodEntry=_DlmodEntry_Object((1,3,6,1,4,1,2021,13,14,2,1))
dlmodEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dlmodEntry.setStatus(_A)
class _DlmodIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DlmodIndex_Type.__name__=_B
_DlmodIndex_Object=MibTableColumn
dlmodIndex=_DlmodIndex_Object((1,3,6,1,4,1,2021,13,14,2,1,1),_DlmodIndex_Type())
dlmodIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dlmodIndex.setStatus(_A)
_DlmodName_Type=DisplayString
_DlmodName_Object=MibTableColumn
dlmodName=_DlmodName_Object((1,3,6,1,4,1,2021,13,14,2,1,2),_DlmodName_Type())
dlmodName.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmodName.setStatus(_A)
_DlmodPath_Type=DisplayString
_DlmodPath_Object=MibTableColumn
dlmodPath=_DlmodPath_Object((1,3,6,1,4,1,2021,13,14,2,1,3),_DlmodPath_Type())
dlmodPath.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmodPath.setStatus(_A)
_DlmodError_Type=DisplayString
_DlmodError_Object=MibTableColumn
dlmodError=_DlmodError_Object((1,3,6,1,4,1,2021,13,14,2,1,4),_DlmodError_Type())
dlmodError.setMaxAccess(_D)
if mibBuilder.loadTexts:dlmodError.setStatus(_A)
class _DlmodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('loaded',1),('unloaded',2),('error',3),('load',4),('unload',5),('create',6),('delete',7)))
_DlmodStatus_Type.__name__=_B
_DlmodStatus_Object=MibTableColumn
dlmodStatus=_DlmodStatus_Object((1,3,6,1,4,1,2021,13,14,2,1,5),_DlmodStatus_Type())
dlmodStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dlmodStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ucdDlmodMIB':ucdDlmodMIB,'dlmodNextIndex':dlmodNextIndex,'dlmodTable':dlmodTable,'dlmodEntry':dlmodEntry,_F:dlmodIndex,'dlmodName':dlmodName,'dlmodPath':dlmodPath,'dlmodError':dlmodError,'dlmodStatus':dlmodStatus})