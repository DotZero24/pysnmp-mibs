_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mellanoxConfigDB,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxConfigDB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxConfigDBMib=ModuleIdentity((1,3,6,1,4,1,33049,12,1))
if mibBuilder.loadTexts:mellanoxConfigDBMib.setRevisions(('2017-07-25 00:00',))
_MellanoxConfigDBMibObjects_ObjectIdentity=ObjectIdentity
mellanoxConfigDBMibObjects=_MellanoxConfigDBMibObjects_ObjectIdentity((1,3,6,1,4,1,33049,12,1,1))
_MellanoxConfigDBCmd_ObjectIdentity=ObjectIdentity
mellanoxConfigDBCmd=_MellanoxConfigDBCmd_ObjectIdentity((1,3,6,1,4,1,33049,12,1,1,2))
_MellanoxConfigDBCmdUri_Type=OctetString
_MellanoxConfigDBCmdUri_Object=MibScalar
mellanoxConfigDBCmdUri=_MellanoxConfigDBCmdUri_Object((1,3,6,1,4,1,33049,12,1,1,2,1),_MellanoxConfigDBCmdUri_Type())
mellanoxConfigDBCmdUri.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxConfigDBCmdUri.setStatus(_A)
_MellanoxConfigDBCmdFilename_Type=OctetString
_MellanoxConfigDBCmdFilename_Object=MibScalar
mellanoxConfigDBCmdFilename=_MellanoxConfigDBCmdFilename_Object((1,3,6,1,4,1,33049,12,1,1,2,2),_MellanoxConfigDBCmdFilename_Type())
mellanoxConfigDBCmdFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxConfigDBCmdFilename.setStatus(_A)
class _MellanoxConfigDBCmdExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('mellanoxConfigDBCmdExecuteBinarySwitchTo',1),('mellanoxConfigDBCmdExecuteTextApply',2),('mellanoxConfigDBCmdExecuteTextApplyFailContinue',3),('mellanoxConfigDBCmdExecuteBinaryUpload',4),('mellanoxConfigDBCmdExecuteTextUpload',5),('mellanoxConfigDBCmdExecuteConfigWrite',6),('mellanoxConfigDBCmdExecuteBinaryDelete',7),('mellanoxConfigDBCmdExecuteTextDelete',8)))
_MellanoxConfigDBCmdExecute_Type.__name__=_C
_MellanoxConfigDBCmdExecute_Object=MibScalar
mellanoxConfigDBCmdExecute=_MellanoxConfigDBCmdExecute_Object((1,3,6,1,4,1,33049,12,1,1,2,3),_MellanoxConfigDBCmdExecute_Type())
mellanoxConfigDBCmdExecute.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxConfigDBCmdExecute.setStatus(_A)
_MellanoxConfigDBCmdStatus_Type=Integer32
_MellanoxConfigDBCmdStatus_Object=MibScalar
mellanoxConfigDBCmdStatus=_MellanoxConfigDBCmdStatus_Object((1,3,6,1,4,1,33049,12,1,1,2,4),_MellanoxConfigDBCmdStatus_Type())
mellanoxConfigDBCmdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mellanoxConfigDBCmdStatus.setStatus(_A)
_MellanoxConfigDBCmdStatusString_Type=OctetString
_MellanoxConfigDBCmdStatusString_Object=MibScalar
mellanoxConfigDBCmdStatusString=_MellanoxConfigDBCmdStatusString_Object((1,3,6,1,4,1,33049,12,1,1,2,5),_MellanoxConfigDBCmdStatusString_Type())
mellanoxConfigDBCmdStatusString.setMaxAccess(_D)
if mibBuilder.loadTexts:mellanoxConfigDBCmdStatusString.setStatus(_A)
mibBuilder.exportSymbols('MELLANOX-CONFIG-DB-MIB',**{'mellanoxConfigDBMib':mellanoxConfigDBMib,'mellanoxConfigDBMibObjects':mellanoxConfigDBMibObjects,'mellanoxConfigDBCmd':mellanoxConfigDBCmd,'mellanoxConfigDBCmdUri':mellanoxConfigDBCmdUri,'mellanoxConfigDBCmdFilename':mellanoxConfigDBCmdFilename,'mellanoxConfigDBCmdExecute':mellanoxConfigDBCmdExecute,'mellanoxConfigDBCmdStatus':mellanoxConfigDBCmdStatus,'mellanoxConfigDBCmdStatusString':mellanoxConfigDBCmdStatusString})