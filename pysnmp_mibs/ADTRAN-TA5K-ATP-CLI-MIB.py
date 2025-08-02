_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adGenTa5kAtpCli,adGenTa5kAtpCliID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kAtpCli','adGenTa5kAtpCliID')
adIdentity,adIdentityShared,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adIdentityShared','adMgmt','adProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kAtpCliModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,4,1))
_AdTa5kAtpCliTable_Object=MibTable
adTa5kAtpCliTable=_AdTa5kAtpCliTable_Object((1,3,6,1,4,1,664,5,67,1,4,1))
if mibBuilder.loadTexts:adTa5kAtpCliTable.setStatus(_A)
_AdTa5kAtpCliEntry_Object=MibTableRow
adTa5kAtpCliEntry=_AdTa5kAtpCliEntry_Object((1,3,6,1,4,1,664,5,67,1,4,1,1))
adTa5kAtpCliEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTa5kAtpCliEntry.setStatus(_A)
_AdTa5kAtpCliCommand_Type=DisplayString
_AdTa5kAtpCliCommand_Object=MibTableColumn
adTa5kAtpCliCommand=_AdTa5kAtpCliCommand_Object((1,3,6,1,4,1,664,5,67,1,4,1,1,1),_AdTa5kAtpCliCommand_Type())
adTa5kAtpCliCommand.setMaxAccess('read-write')
if mibBuilder.loadTexts:adTa5kAtpCliCommand.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-ATP-CLI-MIB',**{'adTa5kAtpCliTable':adTa5kAtpCliTable,'adTa5kAtpCliEntry':adTa5kAtpCliEntry,'adTa5kAtpCliCommand':adTa5kAtpCliCommand,'adTa5kAtpCliModuleIdentity':adTa5kAtpCliModuleIdentity})