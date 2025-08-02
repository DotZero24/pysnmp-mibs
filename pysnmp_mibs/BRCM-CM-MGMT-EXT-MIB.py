_E='cmScanIndex'
_D='BRCM-CM-MGMT-EXT-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
broadcomCableDataMgmt,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','broadcomCableDataMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cmMgmtExt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,99,4413,2))
if mibBuilder.loadTexts:cmMgmtExt.setRevisions(('2007-02-05 00:00','2005-04-18 00:00'))
_CmMgmtExtBase_ObjectIdentity=ObjectIdentity
cmMgmtExtBase=_CmMgmtExtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,99,4413,2,1))
class _CmMgmtExtBaseStandbySwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CmMgmtExtBaseStandbySwitchStatus_Type.__name__=_B
_CmMgmtExtBaseStandbySwitchStatus_Object=MibScalar
cmMgmtExtBaseStandbySwitchStatus=_CmMgmtExtBaseStandbySwitchStatus_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,1,1),_CmMgmtExtBaseStandbySwitchStatus_Type())
cmMgmtExtBaseStandbySwitchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmMgmtExtBaseStandbySwitchStatus.setStatus(_A)
_CmMgmtExtScan_ObjectIdentity=ObjectIdentity
cmMgmtExtScan=_CmMgmtExtScan_ObjectIdentity((1,3,6,1,4,1,4413,2,2,99,4413,2,2))
class _CmScanPushFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CmScanPushFrequency_Type.__name__=_B
_CmScanPushFrequency_Object=MibScalar
cmScanPushFrequency=_CmScanPushFrequency_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,2,1),_CmScanPushFrequency_Type())
cmScanPushFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cmScanPushFrequency.setStatus(_A)
_CmScanTable_Object=MibTable
cmScanTable=_CmScanTable_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,2,2))
if mibBuilder.loadTexts:cmScanTable.setStatus(_A)
_CmScanEntry_Object=MibTableRow
cmScanEntry=_CmScanEntry_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,2,2,1))
cmScanEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cmScanEntry.setStatus(_A)
class _CmScanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CmScanIndex_Type.__name__=_B
_CmScanIndex_Object=MibTableColumn
cmScanIndex=_CmScanIndex_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,2,2,1,1),_CmScanIndex_Type())
cmScanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cmScanIndex.setStatus(_A)
_CmScanFrequency_Type=Integer32
_CmScanFrequency_Object=MibTableColumn
cmScanFrequency=_CmScanFrequency_Object((1,3,6,1,4,1,4413,2,2,99,4413,2,2,2,1,2),_CmScanFrequency_Type())
cmScanFrequency.setMaxAccess('read-only')
if mibBuilder.loadTexts:cmScanFrequency.setStatus(_A)
if mibBuilder.loadTexts:cmScanFrequency.setUnits('hertz')
mibBuilder.exportSymbols(_D,**{'cmMgmtExt':cmMgmtExt,'cmMgmtExtBase':cmMgmtExtBase,'cmMgmtExtBaseStandbySwitchStatus':cmMgmtExtBaseStandbySwitchStatus,'cmMgmtExtScan':cmMgmtExtScan,'cmScanPushFrequency':cmScanPushFrequency,'cmScanTable':cmScanTable,'cmScanEntry':cmScanEntry,_E:cmScanIndex,'cmScanFrequency':cmScanFrequency})