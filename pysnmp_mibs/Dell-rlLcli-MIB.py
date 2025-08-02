_H='rlLcliCommandLevelContextName'
_G='rlLcliCommandLevelCommandName'
_F='Integer32'
_E='Dell-rlLcli-MIB'
_D='TruthValue'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
rlLCli=ModuleIdentity((1,3,6,1,4,1,89,74))
if mibBuilder.loadTexts:rlLCli.setRevisions(('2007-07-26 00:00','2005-04-11 00:00','2005-03-28 00:00','2004-03-26 00:00'))
_RlLCliMibVersion_Type=Integer32
_RlLCliMibVersion_Object=MibScalar
rlLCliMibVersion=_RlLCliMibVersion_Object((1,3,6,1,4,1,89,74,1),_RlLCliMibVersion_Type())
rlLCliMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlLCliMibVersion.setStatus(_A)
class _RlLCliTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3932159))
_RlLCliTimeout_Type.__name__=_C
_RlLCliTimeout_Object=MibScalar
rlLCliTimeout=_RlLCliTimeout_Object((1,3,6,1,4,1,89,74,2),_RlLCliTimeout_Type())
rlLCliTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliTimeout.setStatus(_A)
class _RlLCliHistoryEnable_Type(TruthValue):defaultValue=1
_RlLCliHistoryEnable_Type.__name__=_D
_RlLCliHistoryEnable_Object=MibScalar
rlLCliHistoryEnable=_RlLCliHistoryEnable_Object((1,3,6,1,4,1,89,74,3),_RlLCliHistoryEnable_Type())
rlLCliHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliHistoryEnable.setStatus(_A)
class _RlLCliHistorySize_Type(Unsigned32):defaultValue=10
_RlLCliHistorySize_Type.__name__=_C
_RlLCliHistorySize_Object=MibScalar
rlLCliHistorySize=_RlLCliHistorySize_Object((1,3,6,1,4,1,89,74,4),_RlLCliHistorySize_Type())
rlLCliHistorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliHistorySize.setStatus(_A)
_RlLcliCommandLevelTable_Object=MibTable
rlLcliCommandLevelTable=_RlLcliCommandLevelTable_Object((1,3,6,1,4,1,89,74,5))
if mibBuilder.loadTexts:rlLcliCommandLevelTable.setStatus(_A)
_RlLcliCommandLevelEntry_Object=MibTableRow
rlLcliCommandLevelEntry=_RlLcliCommandLevelEntry_Object((1,3,6,1,4,1,89,74,5,1))
rlLcliCommandLevelEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:rlLcliCommandLevelEntry.setStatus(_A)
_RlLcliCommandLevelCommandName_Type=DisplayString
_RlLcliCommandLevelCommandName_Object=MibTableColumn
rlLcliCommandLevelCommandName=_RlLcliCommandLevelCommandName_Object((1,3,6,1,4,1,89,74,5,1,1),_RlLcliCommandLevelCommandName_Type())
rlLcliCommandLevelCommandName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelCommandName.setStatus(_A)
_RlLcliCommandLevelContextName_Type=DisplayString
_RlLcliCommandLevelContextName_Object=MibTableColumn
rlLcliCommandLevelContextName=_RlLcliCommandLevelContextName_Object((1,3,6,1,4,1,89,74,5,1,2),_RlLcliCommandLevelContextName_Type())
rlLcliCommandLevelContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelContextName.setStatus(_A)
_RlLcliCommandLevelInsertTime_Type=TimeTicks
_RlLcliCommandLevelInsertTime_Object=MibTableColumn
rlLcliCommandLevelInsertTime=_RlLcliCommandLevelInsertTime_Object((1,3,6,1,4,1,89,74,5,1,3),_RlLcliCommandLevelInsertTime_Type())
rlLcliCommandLevelInsertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelInsertTime.setStatus(_A)
_RlLcliCommandLevelCommandLevel_Type=Integer32
_RlLcliCommandLevelCommandLevel_Object=MibTableColumn
rlLcliCommandLevelCommandLevel=_RlLcliCommandLevelCommandLevel_Object((1,3,6,1,4,1,89,74,5,1,4),_RlLcliCommandLevelCommandLevel_Type())
rlLcliCommandLevelCommandLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelCommandLevel.setStatus(_A)
class _RlLcliCommandLevelActionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('set',1),('reset',2),('setAll',3),('resetAll',4)))
_RlLcliCommandLevelActionMode_Type.__name__=_F
_RlLcliCommandLevelActionMode_Object=MibTableColumn
rlLcliCommandLevelActionMode=_RlLcliCommandLevelActionMode_Object((1,3,6,1,4,1,89,74,5,1,5),_RlLcliCommandLevelActionMode_Type())
rlLcliCommandLevelActionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelActionMode.setStatus(_A)
_RlLcliCommandLevelStatus_Type=RowStatus
_RlLcliCommandLevelStatus_Object=MibTableColumn
rlLcliCommandLevelStatus=_RlLcliCommandLevelStatus_Object((1,3,6,1,4,1,89,74,5,1,6),_RlLcliCommandLevelStatus_Type())
rlLcliCommandLevelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLcliCommandLevelStatus.setStatus(_A)
class _RlLCliSshTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3932159))
_RlLCliSshTimeout_Type.__name__=_C
_RlLCliSshTimeout_Object=MibScalar
rlLCliSshTimeout=_RlLCliSshTimeout_Object((1,3,6,1,4,1,89,74,6),_RlLCliSshTimeout_Type())
rlLCliSshTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliSshTimeout.setStatus(_A)
class _RlLCliTelnetTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3932159))
_RlLCliTelnetTimeout_Type.__name__=_C
_RlLCliTelnetTimeout_Object=MibScalar
rlLCliTelnetTimeout=_RlLCliTelnetTimeout_Object((1,3,6,1,4,1,89,74,7),_RlLCliTelnetTimeout_Type())
rlLCliTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliTelnetTimeout.setStatus(_A)
class _RlLCliTelnetHistoryEnable_Type(TruthValue):defaultValue=1
_RlLCliTelnetHistoryEnable_Type.__name__=_D
_RlLCliTelnetHistoryEnable_Object=MibScalar
rlLCliTelnetHistoryEnable=_RlLCliTelnetHistoryEnable_Object((1,3,6,1,4,1,89,74,8),_RlLCliTelnetHistoryEnable_Type())
rlLCliTelnetHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliTelnetHistoryEnable.setStatus(_A)
class _RlLCliTelnetHistorySize_Type(Unsigned32):defaultValue=10
_RlLCliTelnetHistorySize_Type.__name__=_C
_RlLCliTelnetHistorySize_Object=MibScalar
rlLCliTelnetHistorySize=_RlLCliTelnetHistorySize_Object((1,3,6,1,4,1,89,74,9),_RlLCliTelnetHistorySize_Type())
rlLCliTelnetHistorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliTelnetHistorySize.setStatus(_A)
class _RlLCliSshHistoryEnable_Type(TruthValue):defaultValue=1
_RlLCliSshHistoryEnable_Type.__name__=_D
_RlLCliSshHistoryEnable_Object=MibScalar
rlLCliSshHistoryEnable=_RlLCliSshHistoryEnable_Object((1,3,6,1,4,1,89,74,10),_RlLCliSshHistoryEnable_Type())
rlLCliSshHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliSshHistoryEnable.setStatus(_A)
class _RlLCliSshHistorySize_Type(Unsigned32):defaultValue=10
_RlLCliSshHistorySize_Type.__name__=_C
_RlLCliSshHistorySize_Object=MibScalar
rlLCliSshHistorySize=_RlLCliSshHistorySize_Object((1,3,6,1,4,1,89,74,11),_RlLCliSshHistorySize_Type())
rlLCliSshHistorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLCliSshHistorySize.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlLCli':rlLCli,'rlLCliMibVersion':rlLCliMibVersion,'rlLCliTimeout':rlLCliTimeout,'rlLCliHistoryEnable':rlLCliHistoryEnable,'rlLCliHistorySize':rlLCliHistorySize,'rlLcliCommandLevelTable':rlLcliCommandLevelTable,'rlLcliCommandLevelEntry':rlLcliCommandLevelEntry,_G:rlLcliCommandLevelCommandName,_H:rlLcliCommandLevelContextName,'rlLcliCommandLevelInsertTime':rlLcliCommandLevelInsertTime,'rlLcliCommandLevelCommandLevel':rlLcliCommandLevelCommandLevel,'rlLcliCommandLevelActionMode':rlLcliCommandLevelActionMode,'rlLcliCommandLevelStatus':rlLcliCommandLevelStatus,'rlLCliSshTimeout':rlLCliSshTimeout,'rlLCliTelnetTimeout':rlLCliTelnetTimeout,'rlLCliTelnetHistoryEnable':rlLCliTelnetHistoryEnable,'rlLCliTelnetHistorySize':rlLCliTelnetHistorySize,'rlLCliSshHistoryEnable':rlLCliSshHistoryEnable,'rlLCliSshHistorySize':rlLCliSshHistorySize})