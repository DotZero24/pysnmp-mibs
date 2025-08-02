_E='snsAuthUsersIPAddr'
_D='STORMSHIELD-AUTHUSERS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsUsers=ModuleIdentity((1,3,6,1,4,1,11256,1,2))
if mibBuilder.loadTexts:snsUsers.setRevisions(('2017-02-20 00:00',))
_SnsAuthUsersTable_Object=MibTable
snsAuthUsersTable=_SnsAuthUsersTable_Object((1,3,6,1,4,1,11256,1,2,1))
if mibBuilder.loadTexts:snsAuthUsersTable.setStatus(_A)
_SnsAuthUsersEntry_Object=MibTableRow
snsAuthUsersEntry=_SnsAuthUsersEntry_Object((1,3,6,1,4,1,11256,1,2,1,1))
snsAuthUsersEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsAuthUsersEntry.setStatus(_A)
class _SnsAuthUsersIPAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnsAuthUsersIPAddr_Type.__name__=_C
_SnsAuthUsersIPAddr_Object=MibTableColumn
snsAuthUsersIPAddr=_SnsAuthUsersIPAddr_Object((1,3,6,1,4,1,11256,1,2,1,1,1),_SnsAuthUsersIPAddr_Type())
snsAuthUsersIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAuthUsersIPAddr.setStatus(_A)
_SnsAuthUsersTimeOut_Type=Counter64
_SnsAuthUsersTimeOut_Object=MibTableColumn
snsAuthUsersTimeOut=_SnsAuthUsersTimeOut_Object((1,3,6,1,4,1,11256,1,2,1,1,2),_SnsAuthUsersTimeOut_Type())
snsAuthUsersTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAuthUsersTimeOut.setStatus(_A)
_SnsAuthUsersName_Type=SnmpAdminString
_SnsAuthUsersName_Object=MibTableColumn
snsAuthUsersName=_SnsAuthUsersName_Object((1,3,6,1,4,1,11256,1,2,1,1,3),_SnsAuthUsersName_Type())
snsAuthUsersName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAuthUsersName.setStatus(_A)
_SnsAuthUsersDomain_Type=SnmpAdminString
_SnsAuthUsersDomain_Object=MibTableColumn
snsAuthUsersDomain=_SnsAuthUsersDomain_Object((1,3,6,1,4,1,11256,1,2,1,1,4),_SnsAuthUsersDomain_Type())
snsAuthUsersDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAuthUsersDomain.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsUsers':snsUsers,'snsAuthUsersTable':snsAuthUsersTable,'snsAuthUsersEntry':snsAuthUsersEntry,_E:snsAuthUsersIPAddr,'snsAuthUsersTimeOut':snsAuthUsersTimeOut,'snsAuthUsersName':snsAuthUsersName,'snsAuthUsersDomain':snsAuthUsersDomain})