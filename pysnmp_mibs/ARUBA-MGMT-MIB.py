_C='Integer32'
_B='not-accessible'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaMgmt,=mibBuilder.importSymbols('ARUBA-MIB','arubaMgmt')
ArubaEnableValue,=mibBuilder.importSymbols('ARUBA-TC','ArubaEnableValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
arubaMgmtExtensions=ModuleIdentity((1,3,6,1,4,1,14823,3,3))
_ArubaMgmtGroup_ObjectIdentity=ObjectIdentity
arubaMgmtGroup=_ArubaMgmtGroup_ObjectIdentity((1,3,6,1,4,1,14823,3,3,1))
_ArubaGetTable_Type=ObjectIdentifier
_ArubaGetTable_Object=MibScalar
arubaGetTable=_ArubaGetTable_Object((1,3,6,1,4,1,14823,3,3,1,1),_ArubaGetTable_Type())
arubaGetTable.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaGetTable.setStatus(_A)
_ArubaNumberOfRows_Type=Integer32
_ArubaNumberOfRows_Object=MibScalar
arubaNumberOfRows=_ArubaNumberOfRows_Object((1,3,6,1,4,1,14823,3,3,1,2),_ArubaNumberOfRows_Type())
arubaNumberOfRows.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaNumberOfRows.setStatus(_A)
_ArubaRowInstance_Type=ObjectIdentifier
_ArubaRowInstance_Object=MibScalar
arubaRowInstance=_ArubaRowInstance_Object((1,3,6,1,4,1,14823,3,3,1,3),_ArubaRowInstance_Type())
arubaRowInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaRowInstance.setStatus(_A)
class _ArubaGetTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('endTable',1),('moreTable',2),('retrieveError',3),('noAmpSupport',4),('invalidColumnID',5),('resourceAllocationFailure',6)))
_ArubaGetTableStatus_Type.__name__=_C
_ArubaGetTableStatus_Object=MibScalar
arubaGetTableStatus=_ArubaGetTableStatus_Object((1,3,6,1,4,1,14823,3,3,1,4),_ArubaGetTableStatus_Type())
arubaGetTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaGetTableStatus.setStatus(_A)
_ArubaNumberOfColumns_Type=Integer32
_ArubaNumberOfColumns_Object=MibScalar
arubaNumberOfColumns=_ArubaNumberOfColumns_Object((1,3,6,1,4,1,14823,3,3,1,5),_ArubaNumberOfColumns_Type())
arubaNumberOfColumns.setMaxAccess(_B)
if mibBuilder.loadTexts:arubaNumberOfColumns.setStatus(_A)
_ArubaSwitchAMPSupport_Type=ArubaEnableValue
_ArubaSwitchAMPSupport_Object=MibScalar
arubaSwitchAMPSupport=_ArubaSwitchAMPSupport_Object((1,3,6,1,4,1,14823,3,3,1,6),_ArubaSwitchAMPSupport_Type())
arubaSwitchAMPSupport.setMaxAccess('read-only')
if mibBuilder.loadTexts:arubaSwitchAMPSupport.setStatus(_A)
mibBuilder.exportSymbols('ARUBA-MGMT-MIB',**{'arubaMgmtExtensions':arubaMgmtExtensions,'arubaMgmtGroup':arubaMgmtGroup,'arubaGetTable':arubaGetTable,'arubaNumberOfRows':arubaNumberOfRows,'arubaRowInstance':arubaRowInstance,'arubaGetTableStatus':arubaGetTableStatus,'arubaNumberOfColumns':arubaNumberOfColumns,'arubaSwitchAMPSupport':arubaSwitchAMPSupport})