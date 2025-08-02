_C='IONLINE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','snmpModules')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
elite=ModuleIdentity((1,3,6,1,4,1,21068))
_Ionline_ObjectIdentity=ObjectIdentity
ionline=_Ionline_ObjectIdentity((1,3,6,1,4,1,21068,1))
if mibBuilder.loadTexts:ionline.setStatus(_A)
_IoPoolStatus_ObjectIdentity=ObjectIdentity
ioPoolStatus=_IoPoolStatus_ObjectIdentity((1,3,6,1,4,1,21068,1,3))
_IoPoolUsage_Type=Integer32
_IoPoolUsage_Object=MibScalar
ioPoolUsage=_IoPoolUsage_Object((1,3,6,1,4,1,21068,1,3,1),_IoPoolUsage_Type())
ioPoolUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ioPoolUsage.setStatus(_A)
_IoPoolTable_Object=MibTable
ioPoolTable=_IoPoolTable_Object((1,3,6,1,4,1,21068,2))
if mibBuilder.loadTexts:ioPoolTable.setStatus(_A)
_IoPoolEntry_Object=MibTableRow
ioPoolEntry=_IoPoolEntry_Object((1,3,6,1,4,1,21068,2,1))
ioPoolEntry.setIndexNames((0,_C,'sysORIndex'))
if mibBuilder.loadTexts:ioPoolEntry.setStatus(_A)
_IoPoolORId_Type=ObjectIdentifier
_IoPoolORId_Object=MibTableColumn
ioPoolORId=_IoPoolORId_Object((1,3,6,1,4,1,21068,2,1,2),_IoPoolORId_Type())
ioPoolORId.setMaxAccess(_B)
if mibBuilder.loadTexts:ioPoolORId.setStatus(_A)
_IoPoolORDescr_Type=DisplayString
_IoPoolORDescr_Object=MibTableColumn
ioPoolORDescr=_IoPoolORDescr_Object((1,3,6,1,4,1,21068,2,1,3),_IoPoolORDescr_Type())
ioPoolORDescr.setMaxAccess('read-only')
if mibBuilder.loadTexts:ioPoolORDescr.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'elite':elite,'ionline':ionline,'ioPoolStatus':ioPoolStatus,'ioPoolUsage':ioPoolUsage,'ioPoolTable':ioPoolTable,'ioPoolEntry':ioPoolEntry,'ioPoolORId':ioPoolORId,'ioPoolORDescr':ioPoolORDescr})