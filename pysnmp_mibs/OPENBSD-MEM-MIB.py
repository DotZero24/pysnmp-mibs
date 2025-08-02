_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,ifNumber=mibBuilder.importSymbols(_C,_D,'ifNumber')
openBSD,=mibBuilder.importSymbols('OPENBSD-BASE-MIB','openBSD')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
memMIBObjects=ModuleIdentity((1,3,6,1,4,1,30155,5))
if mibBuilder.loadTexts:memMIBObjects.setRevisions(('2012-02-09 00:00','2008-12-23 00:00'))
_MemMIBVersion_Type=Integer32
_MemMIBVersion_Object=MibScalar
memMIBVersion=_MemMIBVersion_Object((1,3,6,1,4,1,30155,5,1),_MemMIBVersion_Type())
memMIBVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:memMIBVersion.setStatus(_A)
_MemIfTable_Object=MibTable
memIfTable=_MemIfTable_Object((1,3,6,1,4,1,30155,5,2))
if mibBuilder.loadTexts:memIfTable.setStatus(_A)
_MemIfEntry_Object=MibTableRow
memIfEntry=_MemIfEntry_Object((1,3,6,1,4,1,30155,5,2,1))
memIfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:memIfEntry.setStatus(_A)
_MemIfName_Type=DisplayString
_MemIfName_Object=MibTableColumn
memIfName=_MemIfName_Object((1,3,6,1,4,1,30155,5,2,1,1),_MemIfName_Type())
memIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:memIfName.setStatus(_A)
_MemIfLiveLocks_Type=Counter64
_MemIfLiveLocks_Object=MibTableColumn
memIfLiveLocks=_MemIfLiveLocks_Object((1,3,6,1,4,1,30155,5,2,1,2),_MemIfLiveLocks_Type())
memIfLiveLocks.setMaxAccess(_B)
if mibBuilder.loadTexts:memIfLiveLocks.setStatus(_A)
mibBuilder.exportSymbols('OPENBSD-MEM-MIB',**{'memMIBObjects':memMIBObjects,'memMIBVersion':memMIBVersion,'memIfTable':memIfTable,'memIfEntry':memIfEntry,'memIfName':memIfName,'memIfLiveLocks':memIfLiveLocks})