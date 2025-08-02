_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,=mibBuilder.importSymbols('HOST-RESOURCES-MIB','InternationalDisplayString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonicwallSMAAppliance,=mibBuilder.importSymbols('SONICWALL-SMA-MIB','sonicwallSMAAppliance')
sonicwallSecurityHistory=ModuleIdentity((1,3,6,1,4,1,8741,8,1,4))
_NumOfLoginDenials_Type=Integer32
_NumOfLoginDenials_Object=MibScalar
numOfLoginDenials=_NumOfLoginDenials_Object((1,3,6,1,4,1,8741,8,1,4,1),_NumOfLoginDenials_Type())
numOfLoginDenials.setMaxAccess(_A)
if mibBuilder.loadTexts:numOfLoginDenials.setStatus(_B)
_LastLoginDenial_ObjectIdentity=ObjectIdentity
lastLoginDenial=_LastLoginDenial_ObjectIdentity((1,3,6,1,4,1,8741,8,1,4,2))
_LastLoginDeniedUser_Type=InternationalDisplayString
_LastLoginDeniedUser_Object=MibScalar
lastLoginDeniedUser=_LastLoginDeniedUser_Object((1,3,6,1,4,1,8741,8,1,4,2,1),_LastLoginDeniedUser_Type())
lastLoginDeniedUser.setMaxAccess(_A)
if mibBuilder.loadTexts:lastLoginDeniedUser.setStatus(_B)
_LastLoginDeniedTime_Type=InternationalDisplayString
_LastLoginDeniedTime_Object=MibScalar
lastLoginDeniedTime=_LastLoginDeniedTime_Object((1,3,6,1,4,1,8741,8,1,4,2,2),_LastLoginDeniedTime_Type())
lastLoginDeniedTime.setMaxAccess(_A)
if mibBuilder.loadTexts:lastLoginDeniedTime.setStatus(_B)
_NumOfAccessDenials_Type=Integer32
_NumOfAccessDenials_Object=MibScalar
numOfAccessDenials=_NumOfAccessDenials_Object((1,3,6,1,4,1,8741,8,1,4,3),_NumOfAccessDenials_Type())
numOfAccessDenials.setMaxAccess(_A)
if mibBuilder.loadTexts:numOfAccessDenials.setStatus(_B)
_LastAccessDenial_ObjectIdentity=ObjectIdentity
lastAccessDenial=_LastAccessDenial_ObjectIdentity((1,3,6,1,4,1,8741,8,1,4,4))
_LastAccessDeniedUser_Type=InternationalDisplayString
_LastAccessDeniedUser_Object=MibScalar
lastAccessDeniedUser=_LastAccessDeniedUser_Object((1,3,6,1,4,1,8741,8,1,4,4,1),_LastAccessDeniedUser_Type())
lastAccessDeniedUser.setMaxAccess(_A)
if mibBuilder.loadTexts:lastAccessDeniedUser.setStatus(_B)
_LastAccessDeniedResource_Type=InternationalDisplayString
_LastAccessDeniedResource_Object=MibScalar
lastAccessDeniedResource=_LastAccessDeniedResource_Object((1,3,6,1,4,1,8741,8,1,4,4,2),_LastAccessDeniedResource_Type())
lastAccessDeniedResource.setMaxAccess(_A)
if mibBuilder.loadTexts:lastAccessDeniedResource.setStatus(_B)
_LastAccessDeniedTime_Type=InternationalDisplayString
_LastAccessDeniedTime_Object=MibScalar
lastAccessDeniedTime=_LastAccessDeniedTime_Object((1,3,6,1,4,1,8741,8,1,4,4,3),_LastAccessDeniedTime_Type())
lastAccessDeniedTime.setMaxAccess(_A)
if mibBuilder.loadTexts:lastAccessDeniedTime.setStatus(_B)
mibBuilder.exportSymbols('SONICWALL-SMA-APPLIANCE-SECURITY-HISTORY-MIB',**{'sonicwallSecurityHistory':sonicwallSecurityHistory,'numOfLoginDenials':numOfLoginDenials,'lastLoginDenial':lastLoginDenial,'lastLoginDeniedUser':lastLoginDeniedUser,'lastLoginDeniedTime':lastLoginDeniedTime,'numOfAccessDenials':numOfAccessDenials,'lastAccessDenial':lastAccessDenial,'lastAccessDeniedUser':lastAccessDeniedUser,'lastAccessDeniedResource':lastAccessDeniedResource,'lastAccessDeniedTime':lastAccessDeniedTime})