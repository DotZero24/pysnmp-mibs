_M='interface8'
_L='interface7'
_K='interface6'
_J='interface5'
_I='interface4'
_H='interface3'
_G='interface2'
_F='interface1'
_E='Unsigned32'
_D='Bits'
_C='DisplayString'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtBase,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtBase')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
httpMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,3))
if mibBuilder.loadTexts:httpMgmt.setRevisions(('2007-02-05 00:00','2004-02-24 00:00'))
class _HttpAdminId_Type(DisplayString):defaultValue=OctetString('')
_HttpAdminId_Type.__name__=_C
_HttpAdminId_Object=MibScalar
httpAdminId=_HttpAdminId_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,1),_HttpAdminId_Type())
httpAdminId.setMaxAccess(_A)
if mibBuilder.loadTexts:httpAdminId.setStatus(_B)
class _HttpAdminPassword_Type(DisplayString):defaultValue=OctetString('')
_HttpAdminPassword_Type.__name__=_C
_HttpAdminPassword_Object=MibScalar
httpAdminPassword=_HttpAdminPassword_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,2),_HttpAdminPassword_Type())
httpAdminPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:httpAdminPassword.setStatus(_B)
class _HttpUserId_Type(DisplayString):defaultValue=OctetString('')
_HttpUserId_Type.__name__=_C
_HttpUserId_Object=MibScalar
httpUserId=_HttpUserId_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,3),_HttpUserId_Type())
httpUserId.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserId.setStatus(_B)
class _HttpUserPassword_Type(DisplayString):defaultValue=OctetString('')
_HttpUserPassword_Type.__name__=_C
_HttpUserPassword_Object=MibScalar
httpUserPassword=_HttpUserPassword_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,4),_HttpUserPassword_Type())
httpUserPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserPassword.setStatus(_B)
class _HttpIpStackInterfaces_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7)))
_HttpIpStackInterfaces_Type.__name__=_D
_HttpIpStackInterfaces_Object=MibScalar
httpIpStackInterfaces=_HttpIpStackInterfaces_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,5),_HttpIpStackInterfaces_Type())
httpIpStackInterfaces.setMaxAccess(_A)
if mibBuilder.loadTexts:httpIpStackInterfaces.setStatus(_B)
class _HttpAdvancedAccessEnabled_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7)))
_HttpAdvancedAccessEnabled_Type.__name__=_D
_HttpAdvancedAccessEnabled_Object=MibScalar
httpAdvancedAccessEnabled=_HttpAdvancedAccessEnabled_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,6),_HttpAdvancedAccessEnabled_Type())
httpAdvancedAccessEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:httpAdvancedAccessEnabled.setStatus(_B)
class _HttpPasswordOfTheDaySeed_Type(DisplayString):defaultValue=OctetString('')
_HttpPasswordOfTheDaySeed_Type.__name__=_C
_HttpPasswordOfTheDaySeed_Object=MibScalar
httpPasswordOfTheDaySeed=_HttpPasswordOfTheDaySeed_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,7),_HttpPasswordOfTheDaySeed_Type())
httpPasswordOfTheDaySeed.setMaxAccess(_A)
if mibBuilder.loadTexts:httpPasswordOfTheDaySeed.setStatus(_B)
class _HttpLoginTimeout_Type(Unsigned32):defaultValue=0
_HttpLoginTimeout_Type.__name__=_E
_HttpLoginTimeout_Object=MibScalar
httpLoginTimeout=_HttpLoginTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,3,8),_HttpLoginTimeout_Type())
httpLoginTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:httpLoginTimeout.setStatus(_B)
if mibBuilder.loadTexts:httpLoginTimeout.setUnits('seconds')
mibBuilder.exportSymbols('BRCM-HTTP-MGMT-MIB',**{'httpMgmt':httpMgmt,'httpAdminId':httpAdminId,'httpAdminPassword':httpAdminPassword,'httpUserId':httpUserId,'httpUserPassword':httpUserPassword,'httpIpStackInterfaces':httpIpStackInterfaces,'httpAdvancedAccessEnabled':httpAdvancedAccessEnabled,'httpPasswordOfTheDaySeed':httpPasswordOfTheDaySeed,'httpLoginTimeout':httpLoginTimeout})