_H='cdEngrEJTAGDBChannel'
_G='cdEngrEJTAGIBChannel'
_F='Unsigned32'
_E='BRCM-CABLEDATA-ENGINEERING-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataPrivateMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-PRIVATE-MIB','cableDataPrivateMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
cableDataEngineering=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,3))
if mibBuilder.loadTexts:cableDataEngineering.setRevisions(('2007-02-05 00:00','2006-11-17 00:00','2002-06-04 00:00'))
_CableDataEngineeringBase_ObjectIdentity=ObjectIdentity
cableDataEngineeringBase=_CableDataEngineeringBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,3,1))
_CdEngrMemAccessAddress_Type=Unsigned32
_CdEngrMemAccessAddress_Object=MibScalar
cdEngrMemAccessAddress=_CdEngrMemAccessAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,1),_CdEngrMemAccessAddress_Type())
cdEngrMemAccessAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrMemAccessAddress.setStatus(_A)
class _CdEngrMemAccessNumBytes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CdEngrMemAccessNumBytes_Type.__name__=_F
_CdEngrMemAccessNumBytes_Object=MibScalar
cdEngrMemAccessNumBytes=_CdEngrMemAccessNumBytes_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,2),_CdEngrMemAccessNumBytes_Type())
cdEngrMemAccessNumBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrMemAccessNumBytes.setStatus(_A)
_CdEngrMemAccessData_Type=Unsigned32
_CdEngrMemAccessData_Object=MibScalar
cdEngrMemAccessData=_CdEngrMemAccessData_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,3),_CdEngrMemAccessData_Type())
cdEngrMemAccessData.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrMemAccessData.setStatus(_A)
class _CdEngrMemAccessCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('read',0),('write',1)))
_CdEngrMemAccessCommand_Type.__name__=_C
_CdEngrMemAccessCommand_Object=MibScalar
cdEngrMemAccessCommand=_CdEngrMemAccessCommand_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,4),_CdEngrMemAccessCommand_Type())
cdEngrMemAccessCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrMemAccessCommand.setStatus(_A)
_CableDataEngineeringEjtag_ObjectIdentity=ObjectIdentity
cableDataEngineeringEjtag=_CableDataEngineeringEjtag_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,3,1,20))
_CdEngrEJTAGTPSelect_Type=Integer32
_CdEngrEJTAGTPSelect_Object=MibScalar
cdEngrEJTAGTPSelect=_CdEngrEJTAGTPSelect_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,1),_CdEngrEJTAGTPSelect_Type())
cdEngrEJTAGTPSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGTPSelect.setStatus(_A)
_CdEngrEJTAGDisableAll_Type=TruthValue
_CdEngrEJTAGDisableAll_Object=MibScalar
cdEngrEJTAGDisableAll=_CdEngrEJTAGDisableAll_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,2),_CdEngrEJTAGDisableAll_Type())
cdEngrEJTAGDisableAll.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDisableAll.setStatus(_A)
_CdEngrEJTAGInstrBrkTable_Object=MibTable
cdEngrEJTAGInstrBrkTable=_CdEngrEJTAGInstrBrkTable_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3))
if mibBuilder.loadTexts:cdEngrEJTAGInstrBrkTable.setStatus(_A)
_CdEngrEJTAGInstrBrkEntry_Object=MibTableRow
cdEngrEJTAGInstrBrkEntry=_CdEngrEJTAGInstrBrkEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1))
cdEngrEJTAGInstrBrkEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:cdEngrEJTAGInstrBrkEntry.setStatus(_A)
class _CdEngrEJTAGIBChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CdEngrEJTAGIBChannel_Type.__name__=_C
_CdEngrEJTAGIBChannel_Object=MibTableColumn
cdEngrEJTAGIBChannel=_CdEngrEJTAGIBChannel_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1,1),_CdEngrEJTAGIBChannel_Type())
cdEngrEJTAGIBChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:cdEngrEJTAGIBChannel.setStatus(_A)
_CdEngrEJTAGIBEnabled_Type=TruthValue
_CdEngrEJTAGIBEnabled_Object=MibTableColumn
cdEngrEJTAGIBEnabled=_CdEngrEJTAGIBEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1,2),_CdEngrEJTAGIBEnabled_Type())
cdEngrEJTAGIBEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGIBEnabled.setStatus(_A)
_CdEngrEJTAGIBAddress_Type=OctetString
_CdEngrEJTAGIBAddress_Object=MibTableColumn
cdEngrEJTAGIBAddress=_CdEngrEJTAGIBAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1,3),_CdEngrEJTAGIBAddress_Type())
cdEngrEJTAGIBAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGIBAddress.setStatus(_A)
_CdEngrEJTAGIBAddrMask_Type=OctetString
_CdEngrEJTAGIBAddrMask_Object=MibTableColumn
cdEngrEJTAGIBAddrMask=_CdEngrEJTAGIBAddrMask_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1,4),_CdEngrEJTAGIBAddrMask_Type())
cdEngrEJTAGIBAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGIBAddrMask.setStatus(_A)
_CdEngrEJTAGIBControl_Type=OctetString
_CdEngrEJTAGIBControl_Object=MibTableColumn
cdEngrEJTAGIBControl=_CdEngrEJTAGIBControl_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,3,1,5),_CdEngrEJTAGIBControl_Type())
cdEngrEJTAGIBControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cdEngrEJTAGIBControl.setStatus(_A)
_CdEngrEJTAGDataBrkTable_Object=MibTable
cdEngrEJTAGDataBrkTable=_CdEngrEJTAGDataBrkTable_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4))
if mibBuilder.loadTexts:cdEngrEJTAGDataBrkTable.setStatus(_A)
_CdEngrEJTAGDataBrkEntry_Object=MibTableRow
cdEngrEJTAGDataBrkEntry=_CdEngrEJTAGDataBrkEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1))
cdEngrEJTAGDataBrkEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:cdEngrEJTAGDataBrkEntry.setStatus(_A)
class _CdEngrEJTAGDBChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CdEngrEJTAGDBChannel_Type.__name__=_C
_CdEngrEJTAGDBChannel_Object=MibTableColumn
cdEngrEJTAGDBChannel=_CdEngrEJTAGDBChannel_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,1),_CdEngrEJTAGDBChannel_Type())
cdEngrEJTAGDBChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:cdEngrEJTAGDBChannel.setStatus(_A)
_CdEngrEJTAGDBEnabled_Type=TruthValue
_CdEngrEJTAGDBEnabled_Object=MibTableColumn
cdEngrEJTAGDBEnabled=_CdEngrEJTAGDBEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,2),_CdEngrEJTAGDBEnabled_Type())
cdEngrEJTAGDBEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDBEnabled.setStatus(_A)
_CdEngrEJTAGDBAddress_Type=OctetString
_CdEngrEJTAGDBAddress_Object=MibTableColumn
cdEngrEJTAGDBAddress=_CdEngrEJTAGDBAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,3),_CdEngrEJTAGDBAddress_Type())
cdEngrEJTAGDBAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDBAddress.setStatus(_A)
_CdEngrEJTAGDBAddrMask_Type=OctetString
_CdEngrEJTAGDBAddrMask_Object=MibTableColumn
cdEngrEJTAGDBAddrMask=_CdEngrEJTAGDBAddrMask_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,4),_CdEngrEJTAGDBAddrMask_Type())
cdEngrEJTAGDBAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDBAddrMask.setStatus(_A)
_CdEngrEJTAGDBDataVal_Type=OctetString
_CdEngrEJTAGDBDataVal_Object=MibTableColumn
cdEngrEJTAGDBDataVal=_CdEngrEJTAGDBDataVal_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,5),_CdEngrEJTAGDBDataVal_Type())
cdEngrEJTAGDBDataVal.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDBDataVal.setStatus(_A)
_CdEngrEJTAGDBDataMask_Type=OctetString
_CdEngrEJTAGDBDataMask_Object=MibTableColumn
cdEngrEJTAGDBDataMask=_CdEngrEJTAGDBDataMask_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,6),_CdEngrEJTAGDBDataMask_Type())
cdEngrEJTAGDBDataMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cdEngrEJTAGDBDataMask.setStatus(_A)
_CdEngrEJTAGDBControl_Type=OctetString
_CdEngrEJTAGDBControl_Object=MibTableColumn
cdEngrEJTAGDBControl=_CdEngrEJTAGDBControl_Object((1,3,6,1,4,1,4413,2,99,1,1,3,1,20,4,1,7),_CdEngrEJTAGDBControl_Type())
cdEngrEJTAGDBControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cdEngrEJTAGDBControl.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cableDataEngineering':cableDataEngineering,'cableDataEngineeringBase':cableDataEngineeringBase,'cdEngrMemAccessAddress':cdEngrMemAccessAddress,'cdEngrMemAccessNumBytes':cdEngrMemAccessNumBytes,'cdEngrMemAccessData':cdEngrMemAccessData,'cdEngrMemAccessCommand':cdEngrMemAccessCommand,'cableDataEngineeringEjtag':cableDataEngineeringEjtag,'cdEngrEJTAGTPSelect':cdEngrEJTAGTPSelect,'cdEngrEJTAGDisableAll':cdEngrEJTAGDisableAll,'cdEngrEJTAGInstrBrkTable':cdEngrEJTAGInstrBrkTable,'cdEngrEJTAGInstrBrkEntry':cdEngrEJTAGInstrBrkEntry,_G:cdEngrEJTAGIBChannel,'cdEngrEJTAGIBEnabled':cdEngrEJTAGIBEnabled,'cdEngrEJTAGIBAddress':cdEngrEJTAGIBAddress,'cdEngrEJTAGIBAddrMask':cdEngrEJTAGIBAddrMask,'cdEngrEJTAGIBControl':cdEngrEJTAGIBControl,'cdEngrEJTAGDataBrkTable':cdEngrEJTAGDataBrkTable,'cdEngrEJTAGDataBrkEntry':cdEngrEJTAGDataBrkEntry,_H:cdEngrEJTAGDBChannel,'cdEngrEJTAGDBEnabled':cdEngrEJTAGDBEnabled,'cdEngrEJTAGDBAddress':cdEngrEJTAGDBAddress,'cdEngrEJTAGDBAddrMask':cdEngrEJTAGDBAddrMask,'cdEngrEJTAGDBDataVal':cdEngrEJTAGDBDataVal,'cdEngrEJTAGDBDataMask':cdEngrEJTAGDBDataMask,'cdEngrEJTAGDBControl':cdEngrEJTAGDBControl})