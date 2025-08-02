_D='OctetString'
_C='current'
_B='read-write'
_A='TimeTicks'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_A,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
begemotHostres=ModuleIdentity((1,3,6,1,4,1,12325,1,202))
if mibBuilder.loadTexts:begemotHostres.setRevisions(('2006-01-03 00:00',))
_BegemotHostresObjects_ObjectIdentity=ObjectIdentity
begemotHostresObjects=_BegemotHostresObjects_ObjectIdentity((1,3,6,1,4,1,12325,1,202,1))
class _BegemotHrStorageUpdate_Type(TimeTicks):defaultValue=700
_BegemotHrStorageUpdate_Type.__name__=_A
_BegemotHrStorageUpdate_Object=MibScalar
begemotHrStorageUpdate=_BegemotHrStorageUpdate_Object((1,3,6,1,4,1,12325,1,202,1,1),_BegemotHrStorageUpdate_Type())
begemotHrStorageUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrStorageUpdate.setStatus(_C)
class _BegemotHrFSUpdate_Type(TimeTicks):defaultValue=700
_BegemotHrFSUpdate_Type.__name__=_A
_BegemotHrFSUpdate_Object=MibScalar
begemotHrFSUpdate=_BegemotHrFSUpdate_Object((1,3,6,1,4,1,12325,1,202,1,2),_BegemotHrFSUpdate_Type())
begemotHrFSUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrFSUpdate.setStatus(_C)
class _BegemotHrDiskStorageUpdate_Type(TimeTicks):defaultValue=300
_BegemotHrDiskStorageUpdate_Type.__name__=_A
_BegemotHrDiskStorageUpdate_Object=MibScalar
begemotHrDiskStorageUpdate=_BegemotHrDiskStorageUpdate_Object((1,3,6,1,4,1,12325,1,202,1,3),_BegemotHrDiskStorageUpdate_Type())
begemotHrDiskStorageUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrDiskStorageUpdate.setStatus(_C)
class _BegemotHrNetworkUpdate_Type(TimeTicks):defaultValue=700
_BegemotHrNetworkUpdate_Type.__name__=_A
_BegemotHrNetworkUpdate_Object=MibScalar
begemotHrNetworkUpdate=_BegemotHrNetworkUpdate_Object((1,3,6,1,4,1,12325,1,202,1,4),_BegemotHrNetworkUpdate_Type())
begemotHrNetworkUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrNetworkUpdate.setStatus(_C)
class _BegemotHrSWInstalledUpdate_Type(TimeTicks):defaultValue=1200
_BegemotHrSWInstalledUpdate_Type.__name__=_A
_BegemotHrSWInstalledUpdate_Object=MibScalar
begemotHrSWInstalledUpdate=_BegemotHrSWInstalledUpdate_Object((1,3,6,1,4,1,12325,1,202,1,5),_BegemotHrSWInstalledUpdate_Type())
begemotHrSWInstalledUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrSWInstalledUpdate.setStatus(_C)
class _BegemotHrSWRunUpdate_Type(TimeTicks):defaultValue=300
_BegemotHrSWRunUpdate_Type.__name__=_A
_BegemotHrSWRunUpdate_Object=MibScalar
begemotHrSWRunUpdate=_BegemotHrSWRunUpdate_Object((1,3,6,1,4,1,12325,1,202,1,6),_BegemotHrSWRunUpdate_Type())
begemotHrSWRunUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrSWRunUpdate.setStatus(_C)
class _BegemotHrPkgDir_Type(OctetString):defaultValue=OctetString('/var/db/pkg')
_BegemotHrPkgDir_Type.__name__=_D
_BegemotHrPkgDir_Object=MibScalar
begemotHrPkgDir=_BegemotHrPkgDir_Object((1,3,6,1,4,1,12325,1,202,1,7),_BegemotHrPkgDir_Type())
begemotHrPkgDir.setMaxAccess(_B)
if mibBuilder.loadTexts:begemotHrPkgDir.setStatus(_C)
mibBuilder.exportSymbols('BEGEMOT-HOSTRES-MIB',**{'begemotHostres':begemotHostres,'begemotHostresObjects':begemotHostresObjects,'begemotHrStorageUpdate':begemotHrStorageUpdate,'begemotHrFSUpdate':begemotHrFSUpdate,'begemotHrDiskStorageUpdate':begemotHrDiskStorageUpdate,'begemotHrNetworkUpdate':begemotHrNetworkUpdate,'begemotHrSWInstalledUpdate':begemotHrSWInstalledUpdate,'begemotHrSWRunUpdate':begemotHrSWRunUpdate,'begemotHrPkgDir':begemotHrPkgDir})