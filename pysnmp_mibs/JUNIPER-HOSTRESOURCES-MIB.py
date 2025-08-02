_D='jnxHrStorageEntry'
_C='JUNIPER-HOSTRESOURCES-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrStorageEntry,=mibBuilder.importSymbols('HOST-RESOURCES-MIB','hrStorageEntry')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxHostResourcesMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,31))
if mibBuilder.loadTexts:jnxHostResourcesMIB.setRevisions(('2004-08-18 00:00','2004-05-05 00:00'))
_JnxHrStorage_ObjectIdentity=ObjectIdentity
jnxHrStorage=_JnxHrStorage_ObjectIdentity((1,3,6,1,4,1,2636,3,31,1))
_JnxHrStorageTable_Object=MibTable
jnxHrStorageTable=_JnxHrStorageTable_Object((1,3,6,1,4,1,2636,3,31,1,1))
if mibBuilder.loadTexts:jnxHrStorageTable.setStatus(_A)
_JnxHrStorageEntry_Object=MibTableRow
jnxHrStorageEntry=_JnxHrStorageEntry_Object((1,3,6,1,4,1,2636,3,31,1,1,1))
if mibBuilder.loadTexts:jnxHrStorageEntry.setStatus(_A)
_JnxHrStoragePercentUsed_Type=Gauge32
_JnxHrStoragePercentUsed_Object=MibTableColumn
jnxHrStoragePercentUsed=_JnxHrStoragePercentUsed_Object((1,3,6,1,4,1,2636,3,31,1,1,1,1),_JnxHrStoragePercentUsed_Type())
jnxHrStoragePercentUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxHrStoragePercentUsed.setStatus(_A)
_JnxHrSystem_ObjectIdentity=ObjectIdentity
jnxHrSystem=_JnxHrSystem_ObjectIdentity((1,3,6,1,4,1,2636,3,31,2))
_JnxHrSystemOpenFiles_Type=Gauge32
_JnxHrSystemOpenFiles_Object=MibScalar
jnxHrSystemOpenFiles=_JnxHrSystemOpenFiles_Object((1,3,6,1,4,1,2636,3,31,2,1),_JnxHrSystemOpenFiles_Type())
jnxHrSystemOpenFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxHrSystemOpenFiles.setStatus(_A)
hrStorageEntry.registerAugmentions((_C,_D))
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'jnxHostResourcesMIB':jnxHostResourcesMIB,'jnxHrStorage':jnxHrStorage,'jnxHrStorageTable':jnxHrStorageTable,_D:jnxHrStorageEntry,'jnxHrStoragePercentUsed':jnxHrStoragePercentUsed,'jnxHrSystem':jnxHrSystem,'jnxHrSystemOpenFiles':jnxHrSystemOpenFiles})